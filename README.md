# IT-Wallet Technical Specifications

[![GitHub release](https://img.shields.io/github/release/italia/eid-wallet-it-docs.svg?style=plastic)](https://github.com/italia/eid-wallet-it-docs/releases)
[![Get invited](https://slack.developers.italia.it/badge.svg)](https://slack.developers.italia.it/)

---

## Table of Contents

- [Intro](#intro)
- [Versioning and preview](#versioning-and-preview)
  - [Branching approach](#branching-approach)
- [Releases](#releases)
- [Contributing](#how-to-contribute)
- [Authors](#authors)
- [License](#license)

## Intro

This repository hosts the IT-Wallet Technical Specifications: the technical architecture, implementation framework and design requirements to be adopoted by the IT-Wallet System Technical Solutions.

For more information on the IT-Wallet System please refer to the [official page]([url](https://innovazione.gov.it/progetti/sistema-it-wallet/)).

The repository is structured as sphinx project tree. **The first stable release is v1.0**; older releases are considered experimental.


## Versioning and preview

This project uses the git *branches* and *tags* in the following way:
* the branch `versione-corrente` contains the current documentation under development;
* The [release page](https://github.com/italia/eid-wallet-it-docs/releases) of
  this project contains all the released versions of the specifications. For the sake of coherence, the *releases* are made according to the tag names.

Each time a release is created or edited, a preview is built based on the tag the release refers to.
A preview of the latest editor's copy build, corresponding to the branch `versione-corrente` can be navigated using the following link:

English version:

 - [Editor's Copy](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/)

Versione Italiana:

 - [Ultima versione in corso di sviluppo](https://italia.github.io/eid-wallet-it-docs/versione-corrente/it/)

### Branching approach

The repository follows a dual-track strategy:

- **Long-Term Support (LTS)** — The 1.4.x series is the LTS line, maintained on the branch `versione-corrente`. This branch receives fixes and minor updates (e.g. 1.4.1, 1.4.2) to ensure stability for production deployments.

- **Future development (EUDIW)** — Milestones from version 1.5 onward are developed on the `eudiw` branch and tagged as separate scopes. This keeps the EUDI Wallet framework evolution distinct from the current LTS documentation.

- **Transition to EUDIW** — When the IT-Wallet is officially notified as an EUDIW-compliant wallet, the `eudiw` branch will be merged into `versione-corrente`. At that point, the LTS line based on 1.4.x will be considered End-of-Life (EOL), and the merged documentation will become the new main specification.

**LTS scope** — For the 1.4.x LTS series, that may be less than 18 months, the period of support is counted from the publication date of the 1.4.0 release tag on GitHub. Within this window, LTS covers:

- **Documentation fixes**: corrections of errors, clarifications, and alignment with implementation findings.
- **Security-related updates**: changes required to reflect security fixes or hardening.
- **Regulatory adjustments**: minor updates needed to stay aligned with national regulation or authoritative guidance, without introducing new features.

LTS does not cover new features, API changes, or modifications that would imply a minor or major version bump beyond the 1.4.x series.

### Releases

This section contains the references about the official releases of this project.

#### Stable release

| Version | English | Italian |
|---------|---------|---------|
| 1.4.6 | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/1.4.6/en/) \| [PDF](https://github.com/italia/eid-wallet-it-docs/releases/download/1.4.6/eid-wallet-it-docs-en-20260806-094556.pdf) | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/1.4.6/it/) \| [PDF](https://github.com/italia/eid-wallet-it-docs/releases/download/1.4.6/eid-wallet-it-docs-it-20260806-094556.pdf) |

For previous releases see [RELEASES-HISTORY.md](RELEASES-HISTORY.md).

## Build Previews

### Using Github Actions

- access the manual [build frontend](https://github.com/italia/eid-wallet-it-docs/actions/workflows/build-html-manual.yml)
- insert the Pull Request number using the form and submit the workflow as shown in the image below.

<img width="1894" height="734" alt="image" src="https://github.com/user-attachments/assets/cdc81d14-4665-41c8-b251-385a1170a299" />


#### Build HTML with Sphinx
````
pip install -r requirements-dev.txt

sphinx-build -b html -d html/en/doctrees docs/en/ html/en
````

ODT
````
sudo apt install pandoc
sphinx-build -b singlehtml docs/en/  html/
cd html
pandoc -o eid-it-wallet-docs.odt index.html
````

### Build PDFs (EN and IT) with Docker

You can build the English and Italian PDFs locally using Docker, without installing LaTeX or Sphinx on your machine.

#### Option A: Use the prebuilt image from GitHub Container Registry

A prebuilt image is published on GitHub Container Registry as [`ghcr.io/italia/eidas-it-wallet-docs-builder`](https://github.com/italia/eid-wallet-it-docs/pkgs/container/eidas-it-wallet-docs-builder).

- **1. Pull the image and tag it as `eid-wallet-it-docs`**

```bash
docker pull ghcr.io/italia/eidas-it-wallet-docs-builder:latest
docker tag ghcr.io/italia/eidas-it-wallet-docs-builder:latest eid-wallet-it-docs
```

You can also use a specific digest or tag shown on the package page, e.g.:

```bash
docker pull ghcr.io/italia/eidas-it-wallet-docs-builder:b235e366abbb852177eb2db39c9b2de2a7b71129
docker tag ghcr.io/italia/eidas-it-wallet-docs-builder:b235e366abbb852177eb2db39c9b2de2a7b71129 eid-wallet-it-docs
```

#### Option B: Build the Docker image locally

From the repository root:

```bash
docker build -t eid-wallet-it-docs .
```

#### Run the container to generate PDFs (shared for both options)

From the repository root:

```bash
docker run --rm \
  -e PDF_BUILD_TAG=1.4.0 \
  -v "$PWD":/workspace \
  -w /workspace \
  eid-wallet-it-docs \
  bash -lc "./utils/build-pdf-local.sh"
```

This command:

- uses the `eid-wallet-it-docs` image (either pulled from GHCR and tagged, or built locally);
- mounts the current repository into `/workspace` inside the container;
- runs `./utils/build-pdf-local.sh`, which for each language in `docs/en` and `docs/it`:
  - builds LaTeX with Sphinx,
  - compiles the main `.tex` file with LuaLaTeX,
  - compresses the PDF with Ghostscript (`/printed`, typically ~35MB → ~16MB),
  - and copies the resulting PDFs into the `pdf_output/` directory in your working tree.

Optional: set `PDF_COMPRESS_SETTINGS=/screen` for a smaller output (~13MB).
## How to contribute


Refer to [Contributing Rules Section](CONTRIBUTING-RULES.md) for an editorial guideline. Don't hesitate to submit [Pull Requests or raise Issues](CONTRIBUTING.md) if you encounter any problems.


## Authors
These Technical Specifications are drafted and maintained by the [Department for Digital Transformation]([url](https://innovazione.gov.it/)), [IPZS Istituto Poligrafico e Zecca dello Stato]([url](https://www.ipzs.it/ext/index.html)) and [PagoPA]([url](https://www.pagopa.it/it/)), with the supervision of [AGID, Agency for Digital Italy]([url](https://www.agid.gov.it/it)). 

## License

The project is covered by a [CC-0](LICENSE) license.
