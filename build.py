import pypandoc
import shutil
from jinja2 import Environment, FileSystemLoader


# get the index.html template
environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("index.html")

# convert home.md to html
homepage_content = pypandoc.convert_file("content/home.md", "html", format="md")
special_edition_content = pypandoc.convert_file(
    "content/special_edition.md", "html", format="md"
)
other_events_content = pypandoc.convert_file(
    "content/other_events.md", "html", format="md"
)

# the navbar to the subpages
subpages_info = [
    ("special_edition", "Teaching Statistics special edition", special_edition_content),
    ("related_events", "Related events", other_events_content),
]

# render index.html
homepage_rendered = template.render(
    title="UKCOTS",
    home="UKCOTS 2024",
    subpages_info=subpages_info,
    content=homepage_content,
)
# write index.html to file
with open("docs/index.html", "w") as f:
    f.write(homepage_rendered)

# render subpages
for fname_basename, label, subpage_content in subpages_info:
    subpage_rendered = template.render(
        title=label,
        home="UKCOTS 2024",
        subpages_info=subpages_info,
        content=subpage_content,
    )
    fname = "docs/" + fname_basename + ".html"

    with open(fname, "w") as f:
        f.write(subpage_rendered)

# copy programme.pdf and abstracts.pdf to docs/
shutil.copyfile("content/programme.pdf", "docs/programme.pdf")
shutil.copyfile("content/abstracts.pdf", "docs/abstracts.pdf")
