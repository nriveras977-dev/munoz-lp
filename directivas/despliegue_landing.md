# SOP: Despliegue y Previsualización Local de Landing Page

## 1. Objetivo
Extraer el código HTML/CSS generado o almacenado desde Google Stitch MCP y levantar un servidor web local accesible desde el navegador del usuario para visualizar y verificar la landing page.

## 2. Entradas
- Archivo de exportación de Stitch (`.system_generated/steps/183/output.txt` o descarga directa vía MCP `download_file`).
- Nombre de la pantalla: `Muñoz - Con Formulario de Cotización WhatsApp` (`projects/8987681311351707660/screens/3a22b6d16ee4442982f7bc20dfa098ac`).

## 3. Salidas
- `index.html` en la raíz del espacio de trabajo con el contenido íntegro y funcional de la landing page.
- Servidor HTTP local ejecutándose en un puerto disponible (ej. 3000 u 8080) fuera del sandbox (`BypassSandbox: true`), permitiendo acceso interactivo desde el navegador del usuario.

## 4. Lógica de Ejecución
1. Parsear el JSON exportado que contiene la clave `html` con el código fuente de la página.
2. Escribir el contenido limpio en `index.html` con codificación UTF-8.
3. Verificar la integridad del archivo `index.html` comprobando que contenga las etiquetas de apertura y cierre de `<html>`.
4. Iniciar el servidor local de Python (`python -m http.server`) o Node.js asegurando el parámetro `BypassSandbox: true` para que sea alcanzable desde el host de Windows.

## 5. Restricciones y Casos Borde
- Nota: En Windows, un servidor iniciado en modo sandbox no es accesible desde el navegador del usuario. Por tanto, el comando que levanta el servidor debe ejecutarse con `BypassSandbox: true`.
- Los caracteres especiales (tildes, eñes) deben preservarse estrictamente en UTF-8.
- Los puertos comunes pueden estar ocupados; se recomienda usar un puerto como 8080 o 3000.
