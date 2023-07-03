# Italian eIDAS Wallet Technical Specifications

[![GitHub release](https://img.shields.io/github/release/italia/eidas-it-wallet-docs.svg?style=plastic)](https://github.com/italia/eidas-it-wallet-docs/releases)
[![Get invited](https://slack.developers.italia.it/badge.svg)](https://slack.developers.italia.it/)
[![Docs Italia](https://docs.italia.it/media/static/projects/badges/passing.svg)](https://docs.italia.it/italia/eidas-it-wallet-docs/it/master/index.html)
[![Documentation](https://img.shields.io/badge/Documentation-Docs%20Italia-blue.svg)](https://docs.italia.it/italia/eidas-it-wallet-docs/)

---

## Table of Contents

- [Description](#description)
- [Documentation](#documentation)
- [Versioning](#versioning)
- [Contributing](#how-to-contribute)
- [Authors](#authors)
- [License](#license)

## Intro

This repository hosts the sphinx project tree of Italian eIDAS Wallet Technical Specifications.

> This repository may contain contents to be considered experimental until the publication of the first release.

## Preview

The stable release in different languages is published at the link below:

 - [English](https://italia.github.io/eidas-it-wallet-docs/versione-corrente/en)
 - [Italian](https://italia.github.io/eidas-it-wallet-docs/versione-corrente/it)

Preview of other branches can be navigated by adding the branch name in the webpath, as follows:

 - https://italia.github.io/eidas-it-wallet-docs/trust-model/en


## Documentation

This repository is structured to be compliant with 
[Docs Italia](https://docs.italia.it/italia/developers-italia/publiccodeyml/it/master/index.html).
This is why the content of the relevant folders will be compiled and rendered inside such platform.
`Docs Italia` is designed to support documents, localized in different languages and for this
reason it is the reference platform for displaying this standard.


## Build

HTML
````
pip install -r requirements.txt

# italian version
sphinx-build -b html -d html/it/doctrees docs/it/  html/it

# english version
sphinx-build -b html -d html/en/doctrees docs/en/  html/en
````

ODT
````
sudo apt install pandoc
sphinx-build -b singlehtml docs/it/  html/
cd html
pandoc -o eidas-it-wallet-docs.odt index.html
````

## Versioning

This project participates in the versioning model [*Semantic
Versioning*](https://semver.org/).

Furthermore, this project uses the git *branches* and *tags* in the following way:
* the branch `versione-corrente` contains the last stable version of the standard;
* The [release page](https://github.com/italia/publiccode.yml/releases) of
  GitHub contains all the released versions of the standard. For the sake of coherence, the *releases* are made according to the tag names.

## How to contribute

Feel free to open [Pull Requests and to present a problem with an Issue](CONTRIBUTING.md).


## License

The project is covered by a [CC-0](LICENSE) license.
