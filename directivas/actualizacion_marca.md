# SOP: Actualización de Marca e Integración de Logotipo

## 1. Objetivo
Actualizar la identidad corporativa de la landing page de "Muñoz Transporte" a "Transportes Milano", procesando el logotipo proporcionado para optimizar su visualización e integrándolo de manera centrada y responsiva en el header y demás puntos de contacto de la landing page.

## 2. Entradas
- Imagen original del logotipo subida por el usuario: `logo.jpg` (resolución original con márgenes).
- Archivo fuente `index.html`.
- Repositorio remoto: `https://github.com/nriveras977-dev/munoz-lp.git` (Rama: `main`).

## 3. Salidas
- Script de procesamiento en `scripts/procesar_logo.py`.
- Logotipo procesado `logo.png` con transparencia y recorte exacto del emblema circular/escudo.
- `index.html` actualizado con la nueva marca "Transportes Milano", logo en el centro del header y coherencia en títulos, textos, formularios y footer.
- Cambios verificados localmente y sincronizados en GitHub.

## 4. Lógica de Ejecución
1. Procesar la imagen del logotipo: detectar el contorno del emblema, recortar de forma cuadrada y generar versión PNG con fondo transparente para perfecta integración sobre fondos oscuros (header) y claros.
2. Actualizar el header en `index.html` para posicionar el logotipo de manera centrada y equilibrada con respecto a los enlaces de navegación y botón de acción.
3. Reemplazar todas las menciones del nombre de marca anterior ("Muñoz") por "Transportes Milano" en meta etiquetas, textos, cotizador WhatsApp y footer.
4. Probar en servidor local `http://localhost:8080`.
5. Ejecutar commit y push al repositorio remoto.

## 5. Restricciones y Casos Borde
- El logotipo original contiene bordes laterales en color crema/blanco cálido. No debe insertarse directamente sin recorte porque alteraría las proporciones y se vería desalineado en contenedores circulares.
- En pantallas móviles, el header debe mantener el logo visible y centrado sin desbordar los botones o enlaces.
- Todos los mensajes preconfigurados de WhatsApp (`msg`) deben reflejar el nuevo nombre "Transportes Milano".
