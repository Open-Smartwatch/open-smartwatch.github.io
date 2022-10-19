# Open Smartwatch Documentation
This repository contains the source code for the Open Smartwatch documentation.

In case you want to compile this documentation yourself, you may use Python Poetry to install the dependencies and then build the documentation using `mkdocs`:

```bash
poetry install
poetry run mkdocs build
```

**Warning** This documentation depends on the [open-smartwatch-os](https://github.com/Open-Smartwatch/open-smartwatch-os) repository and its `docs` folder. If you want to build this documentation locally (and not receive warnings or have incomplete results), you need to clone the `open-smartwatch-os` repository and merge its `docs` folder into this repository's `docs` folder. Furthermore, you'll need to mount its `docs/config.yml` structure into this repository's `mkdocs.yml` file (under `nav.Firmware`). If you are not sure how to do this, you may orient yourself on the [GitHub Actions workflow](.github/workflows/build.yml) that is used to build this documentation.