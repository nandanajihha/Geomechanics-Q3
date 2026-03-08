"""
Script to inject custom CSS into existing HTML file to scale down images
"""

# Read the HTML file
with open('Report exercise Geomechanics and Structural Geology.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Custom CSS to scale down images to 50% size
custom_css = """
<style>
/* Scale down all images to 50% of original size */
.output_png img, .jp-RenderedImage img {
    max-width: 50% !important;
    height: auto !important;
    display: block;
    margin-left: auto;
    margin-right: auto;
}

/* Adjust figure sizes */
.output_subarea img {
    max-width: 50% !important;
}
</style>
"""

# Insert custom CSS before </head>
html_content = html_content.replace('</head>', custom_css + '\n</head>')

# Write back to a new file
with open('Report exercise Geomechanics and Structural Geology_small.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ Done! Created: Report exercise Geomechanics and Structural Geology_small.html")
print("Images are now scaled to 50% of original size")
