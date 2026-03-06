#!/usr/bin/env python3
"""
Fail fast when critical patch markers are missing from the source tree.
This prevents producing a build that compiles but fails at runtime.
"""
import os
import sys


REQUIRED_ANY = [
    (
        "dlls/wow64/process.c",
        ["Wow64SuspendLocalThread", "wow64_NtSuspendThread"],
        "critical wow64 suspend marker"
    ),
]


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: verify_required_markers.py <wine-source-dir>")
        return 1

    wine_src = sys.argv[1]
    errors = []

    for rel_path, needles, label in REQUIRED_ANY:
        full = os.path.join(wine_src, rel_path)
        if not os.path.exists(full):
            errors.append(f"MISSING FILE: {rel_path}")
            continue

        with open(full, errors="replace") as f:
            text = f.read()

        if not any(n in text for n in needles):
            errors.append(
                f"MISSING MARKER: {label} in {rel_path} (expected one of: {', '.join(needles)})"
            )

    if errors:
        print("ERROR: required patch markers missing; refusing to continue")
        for e in errors:
            print(f"  - {e}")
        return 2

    print("verify_required_markers: all required markers present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
