import pypandoc
from jinja2 import Environment, FileSystemLoader


# get the index.html template
environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("index.html")

# convert home.md to html
homepage_content = pypandoc.convert_file("content/home.md", "html", format="md")

# render index.html
homepage_rendered = template.render(title="UKCOTS", home="UKCOTS 2024", content=homepage_content)

# write index.html to file
with open('docs/index.html', 'w') as f:
    f.write(homepage_rendered)
