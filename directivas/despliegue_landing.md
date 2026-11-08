# SOP: Despliegue, Previsualización y Control de Versiones de Landing Page

## 1. Objetivo
Extraer el código HTML/CSS generado o almacenado desde Google Stitch MCP, levantar un servidor web local accesible desde el navegador del usuario para visualizar y verificar la landing page, y mantener el control de versiones sincronizado con el repositorio remoto en GitHub.

## 2. Entradas
- Archivo de exportación de Stitch o descarga directa vía MCP `download_file`.
- Nombre de la pantalla: `Muñoz - Con Formulario de Cotización WhatsApp` (`projects/8987681311351707660/screens/3a22b6d16ee4442982f7bc20dfa098ac`).
- Repositorio remoto: `https://github.com/nriveras977-dev/munoz-lp.git` (Rama: `main`).

## 3. Salidas
- `index.html` en la raíz del espacio de trabajo con el contenido íntegro y funcional de la landing page.
- Servidor HTTP local ejecutándose en un puerto disponible (ej. 8080) fuera del sandbox (`BypassSandbox: true`), permitiendo acceso interactivo desde el navegador del usuario.
- Repositorio Git inicializado y sincronizado en GitHub: `https://github.com/nriveras977-dev/munoz-lp`.

## 4. Lógica de Ejecución
1. Parsear el JSON exportado que contiene la clave `html` con el código fuente de la página.
2. Escribir el contenido limpio en `index.html` con codificación UTF-8.
3. Verificar la integridad del archivo `index.html` comprobando que contenga las etiquetas de apertura y cierre de `<html>`.
4. Iniciar el servidor local de Python (`python -m http.server`) asegurando el parámetro `BypassSandbox: true` para que sea alcanzable desde el host de Windows.
5. Gestionar el control de versiones con Git (agregar archivos, commit descriptivo y push a `origin/main`).

## 5. Restricciones y Casos Borde
- Nota: En Windows, un servidor iniciado en modo sandbox no es accesible desde el navegador del usuario. Por tanto, el comando que levanta el servidor debe ejecutarse con `BypassSandbox: true`.
- Los caracteres especiales (tildes, eñes) deben preservarse estrictamente en UTF-8.
- Las llamadas de red a GitHub (`gh` / `git push`) deben realizarse fuera del sandbox (`BypassSandbox: true`) para permitir el acceso a `api.github.com`.
