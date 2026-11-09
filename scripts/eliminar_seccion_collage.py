import re

def remove_visual_collage_section():
    with open("c:/Users/Usuario/Downloads/muñoz lp/index.html", "r", encoding="utf-8") as f:
        html = f.read()

    pattern = r'\s*<!-- 3\. Floating Visual Collage \(CRITICAL REBUILD\) -->\s*<section class="min-h-\[1400px\].*?</section>'
    
    match = re.search(pattern, html, flags=re.DOTALL)
    if not match:
        raise ValueError("Section not found!")
    
    html_updated = re.sub(pattern, "", html, count=1, flags=re.DOTALL)

    with open("c:/Users/Usuario/Downloads/muñoz lp/index.html", "w", encoding="utf-8") as f:
        f.write(html_updated)
    
    print("Section 'Servicio Ejecutivo & Flota Moderna' removed successfully.")

if __name__ == "__main__":
    remove_visual_collage_section()
