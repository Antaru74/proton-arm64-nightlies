#!/usr/bin/env python3
"""
Patches build-step-arm64ec.sh to use forgiving git apply options for most
patches, but fail hard for known-critical patches required for runtime.
"""
import sys

path = sys.argv[1] if len(sys.argv) > 1 else 'build-scripts/build-step-arm64ec.sh'

with open(path) as f:
    txt = f.read()

txt = txt.replace(
    'git apply ./android/patches/$patch',
    # Fail hard for critical wow64 suspend patch; be forgiving for others.
    'if [ "$patch" = "test-bylaws/dlls_wow64_process_c.patch" ]; then '
    'git apply --ignore-whitespace -C1 ./android/patches/$patch'
    ' || { echo "ERROR: critical patch failed: $patch"; exit 1; }; '
    'else '
    'git apply --ignore-whitespace -C1 ./android/patches/$patch 2>/dev/null'
    ' || git apply --ignore-whitespace -C1 -R --check ./android/patches/$patch 2>/dev/null'
    ' && echo "ALREADY APPLIED (skipped): $patch"'
    ' || echo "WARNING: $patch did not apply and is not already present"; '
    'fi'
)

with open(path, 'w') as f:
    f.write(txt)

print(f"Patched {path}")
