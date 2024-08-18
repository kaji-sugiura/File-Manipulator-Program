import markdown
import sys

markdown_file = "file/markdown.md"
output_file_path = "file/out.html"

markdown_contents = ""

with open(markdown_file) as f:
    markdown_contents = f.read()
    
with open(output_file_path, "w") as f:
    html = markdown.markdown(markdown_contents)
    f.write(html)