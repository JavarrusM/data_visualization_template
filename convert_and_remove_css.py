import nbconvert
import os
import re
from nbconvert import MarkdownExporter
from traitlets.config import Config
import nbformat

# Read the Jupyter Notebook
notebook_path = "analysis.ipynb"
with open(notebook_path, "r", encoding="utf-8") as f:
    notebook = nbformat.read(f, as_version=4)

# Configure the exporter
c = Config()
c.MarkdownExporter.exclude_input = True
c.MarkdownExporter.exclude_input_prompt = True
c.MarkdownExporter.exclude_output_prompt = True
exporter = MarkdownExporter(config=c)

# Export the notebook as Markdown
markdown, resources = exporter.from_notebook_node(notebook)

# Remove CSS code
markdown_no_css = re.sub(
    r"<div>\s*<style scoped>.*?</style>.*?</div>", "", markdown, flags=re.DOTALL
)

# Write the output to the README.md file
output_file = "README.md"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(markdown_no_css)
