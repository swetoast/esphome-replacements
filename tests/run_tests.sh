#!/usr/bin/env bash
# Generates the ESPHome C++ for deltaco-sh-ws03.yaml, extracts the protocol
# lambda and runs it natively against the scenarios in harness.cpp.
# Needs: esphome, g++, python3. Run from the repository root.
set -euo pipefail
cd "$(dirname "$0")/.."
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT

cp deltaco-sh-ws03.yaml "$work/"
key=$(python3 -c "import secrets,base64;print(base64.b64encode(secrets.token_bytes(32)).decode())")
cat > "$work/secrets.yaml" <<SECRETS
wifi_ssid: "test"
wifi_password: "testtest"
ap_password: "testtest"
ota_password: "test"
api_key: "$key"
SECRETS

(cd "$work" && esphome compile --only-generate deltaco-sh-ws03.yaml >/dev/null)
main=$(find "$work/.esphome" -name main.cpp | head -1)

start=$(grep -n '^ *static std::vector<uint8_t> buf;' "$main" | head -1 | cut -d: -f1)
end=$(awk -v s="$start" 'NR > s && /^  }\);/ { print NR; exit }' "$main")
sed -n "$((start - 1)),$((end - 1))p" "$main" > "$work/lambda_body.inc"

cp tests/harness.cpp "$work/"
g++ -std=gnu++20 -Wall -Wextra -Wno-unused-parameter -Wno-missing-field-initializers \
    -I"$work" -o "$work/harness" "$work/harness.cpp"
"$work/harness" | grep -E '^(PASS|FAIL|ALL|FAILED)'
"$work/harness" 2 | grep -E '^(PASS|FAIL|ALL|FAILED)'

python3 -I tests/test_sniff.py tuya_sniff.py
