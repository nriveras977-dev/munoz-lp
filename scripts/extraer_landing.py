import json
from pathlib import Path

def main():
    source_file = Path(r"C:\Users\Usuario\.gemini\antigravity\brain\9b7f67fa-f3c2-4c6f-9d8b-ab524f3f39da\.system_generated\steps\183\output.txt")
    output_html_path = Path("index.html")

    if not source_file.exists():
        raise FileNotFoundError(f"No se encontró el archivo de origen: {source_file}")

    print(f"Leyendo exportación desde: {source_file}")
    with open(source_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    html_content = data.get("html", "")
    if not html_content:
        raise ValueError("El JSON no contiene el campo 'html' con el contenido de la landing.")

    print(f"Escribiendo {len(html_content)} caracteres en {output_html_path}...")
    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print("index.html generado exitosamente.")

if __name__ == "__main__":
    main()
