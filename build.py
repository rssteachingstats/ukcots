import pypandoc
import yaml
import shutil
from jinja2 import Environment, FileSystemLoader


# Get the page.html template.
environment = Environment(loader=FileSystemLoader("templates/"))
page_template = environment.get_template("page.html")

# Get the contents dictionary from the yaml file.
with open("content.yaml") as f:
    content_dict = yaml.safe_load(f)

# This gives us a flat dict of all pages.
pages = {}
pages["main"] = content_dict["main"]
pages.update(content_dict["subpages"])

# This gives the basename and navbar label of subpages
subpages_info = []
for subpage in content_dict["subpages"].values():
    subpages_info.append((subpage["basename"], subpage["navbar"]))

# For the main page and each subpage, render markdown content as html fragement.
html_content = {}
html_rendered = {}
for key, info in pages.items():
    html_fragment = pypandoc.convert_file(info["content"], "html", format="md")
    html_rendered = page_template.render(
        title=info["title"],
        # All pages must contain the same navbar
        # hence, we supply info about the main and subpages
        home_label=pages["main"]["navbar"],
        home_href=pages["main"].get("href", pages["main"]["basename"] + ".html"),
        subpages_info=subpages_info,
        # its content is the rendered fragment
        content=html_fragment,
    )
    fname = "docs/" + info["basename"] + ".html"
    with open(fname, "w") as f:
        f.write(html_rendered)


# copy programme.pdf and abstracts.pdf to docs/
shutil.copyfile("content/programme.pdf", "docs/programme.pdf")
shutil.copyfile("content/abstracts.pdf", "docs/abstracts.pdf")
