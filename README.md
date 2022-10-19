# Open Smartwatch Documentation
This repository contains the source code for the Open Smartwatch documentation.

In case you want to compile this documentation yourself, you may use [Python Poetry](https://python-poetry.org/) to install the dependencies and then build the documentation using `mkdocs`:

```bash
poetry install
poetry run mkdocs build
```

## Warning

This documentation depends on the [open-smartwatch-os](https://github.com/Open-Smartwatch/open-smartwatch-os) repository and its `docs` folder. If you want to build this documentation locally (and not receive warnings or have incomplete results), you need to clone the `open-smartwatch-os` repository and merge its `docs` folder into this repositories `docs` folder. Furthermore, you'll need to mount its `docs/config.yml` structure into this repositories `mkdocs.yml` file (under `nav.Firmware`). If you are not sure how to do this, you may use the Python script `embed_osw_os_docs.py` inside the `.github` folder, which is also used by the GitHub Actions workflow.

```bash
poetry run python .github/embed_osw_os_docs.py
```