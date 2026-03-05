# Proton 10 ARM64 Nightly Builds for Winlator

Automated nightly builds of Wine/Proton for ARM64 Android, packaged as `.wcp` files
for use in Winlator Cmod.

## Quick Start

1. Download the latest `.wcp` from [Releases](../../releases)
2. Import into Winlator: Settings > Wine Version > Import
3. Select the nightly build in your container settings

See [USER_GUIDE.md](docs/USER_GUIDE.md) for detailed installation instructions.

## What's in Each Build

- Wine ARM64 (aarch64) for Android (NDK r27, API 28+)
- ARM64 Windows PE DLLs (aarch64-windows)
- 32-bit Windows PE DLLs (i386-windows) for WoW64
- Default Wine prefix (prefixPack.txz)

## Build Status

Builds run nightly at 2 AM UTC. Check the [Actions tab](../../actions) for status.

## Latest Build

See [latest.json](latest.json) for the current nightly metadata.

## Documentation

| Document | Description |
|----------|-------------|
| [WCP_STRUCTURE.md](docs/WCP_STRUCTURE.md) | .wcp file format, reverse-engineered from reference |
| [BUILD_REQUIREMENTS.md](docs/BUILD_REQUIREMENTS.md) | What you need to build locally |
| [BUILD_ISSUES.md](docs/BUILD_ISSUES.md) | Known problems and solutions |
| [USER_GUIDE.md](docs/USER_GUIDE.md) | How to install and use the builds |
| [DEVELOPER_GUIDE.md](docs/DEVELOPER_GUIDE.md) | How to contribute or customize |

## Key Findings from Analysis

The `.wcp` format (discovered by reverse-engineering the reference build):

- **Compression:** Zstandard (zstd), NOT XZ as assumed
- **profile.json type:** `"Proton"` (not `"Wine"`)
- **Binaries:** Android NDK r27, targeting Android API 28+
- **Structure:** `bin/` + `lib/wine/{aarch64-unix,aarch64-windows,i386-windows}/` + `share/wine/` + `prefixPack.txz`

## Reference Build

The reference `.wcp` analyzed: `Proton-10-arm64ec-controller-fix.wcp` by K11MCH1

- Compressed: 222 MB (Zstandard)
- Uncompressed: 1,436 MB
- Source: https://github.com/K11MCH1/Winlator101

## License

Scripts in this repository are MIT licensed. Wine itself is LGPL.
See [LICENSE](LICENSE) for details.
