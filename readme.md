# Source code for UK Conference on Teaching Statistics website

The UKCOTS website is available at <https://www.ukcots.org>. This repository contains the source code for that website.

## Website content and source files

The [`content.yaml`](`content.yaml`) file contains the skeleton of the website's content, including links to the markdown source files for the main page and each subpage.
To update the content of the website, information in `content.yaml` may need to be changed.
It is more likely, however, that all that will need to change is the contents of the markdown source files for each webpage, which are referenced in `content.yaml`

## To build the website's static html files

```python
# requires pypandoc and Jinja2 and pyyaml
# pip install pypandoc Jinja2 pyyaml
python build.py
```

The static files then go to `docs/`.
When this repo is pushed to GitHub, GitHub pages reads from `docs/` to create a new `github.io` website, which <https://www.ukcots.org> points to.
