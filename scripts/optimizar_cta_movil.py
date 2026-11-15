def optimize_cta_mobile():
    with open("c:/Users/Usuario/Downloads/muñoz lp/index.html", "r", encoding="utf-8") as f:
        html = f.read()

    # Target block from line 180 to 198
    start_tag = '<div class="relative z-10 flex flex-col items-center">'
    end_tag = '</div>\n</div>\n</div>\n</section></main>'

    start_idx = html.find(start_tag)
    end_idx = html.find(end_tag)

    if start_idx == -1 or end_idx == -1:
        raise ValueError(f"Markers not found: start={start_idx}, end={end_idx}")

    new_content = """<div class="relative z-10 flex flex-col items-center w-full">
<img src="logo.png" alt="Transportes Milano" class="w-16 h-16 sm:w-20 sm:h-20 rounded-full object-cover shadow-xl mb-6 sm:mb-8">
<h2 class="font-display text-2xl sm:text-4xl md:text-5xl lg:text-[68px] font-bold text-text tracking-tight leading-tight mb-8 sm:mb-12 max-w-4xl px-2">Experimenta la comodidad de viajar con Transportes Milano</h2>
<div class="flex flex-col sm:flex-row gap-3 sm:gap-6 w-full sm:w-auto max-w-xs sm:max-w-none justify-center items-center">
<button class="w-full sm:w-auto bg-transparent border border-text/30 text-text font-label rounded-full hover:bg-text hover:text-white transition-all duration-300 shrink-0 flex items-center justify-center px-6 text-[11px] h-[44px] font-bold uppercase tracking-wider" onclick="document.getElementById('whatsapp-quote-modal').classList.remove('hidden')">Cotizar traslado</button>
<a href="tel:+56935944255" class="w-full sm:w-auto bg-black text-white font-label rounded-full hover:bg-gray-800 transition-all duration-300 shrink-0 flex items-center justify-center px-6 text-[11px] h-[44px] font-bold uppercase tracking-wider shadow-sm">Llamar ahora</a>
</div>
<div class="flex flex-col sm:flex-row items-center justify-center gap-3 sm:gap-6 mt-8 w-full max-w-md mx-auto text-text/90 font-body-md text-xs sm:text-sm">
<a href="tel:+56935944255" class="flex items-center gap-2.5 px-5 py-3 bg-white rounded-full shadow-sm border border-line/60 hover:border-black/30 transition-all font-medium w-full sm:w-auto justify-center">
<svg class="w-4 h-4 text-[#FF4B2B] shrink-0" fill="currentColor" viewBox="0 0 24 24"><path d="M6.62 10.79a15.05 15.05 0 006.59 6.59l2.2-2.2a1 1 0 011.02-.24 11.4 11.4 0 003.58.57 1 1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1 11.4 11.4 0 00.57 3.58 1 1 0 01-.25 1.02l-2.2 2.19z"></path></svg>
<span>Número: <strong class="text-text font-bold">935 944 255</strong></span>
</a>
<a href="mailto:milano.transporte65@gmail.com" class="flex items-center gap-2.5 px-5 py-3 bg-white rounded-full shadow-sm border border-line/60 hover:border-black/30 transition-all font-medium w-full sm:w-auto justify-center break-all sm:break-normal">
<svg class="w-4 h-4 text-[#8A2387] shrink-0" fill="currentColor" viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"></path></svg>
<span>Correo: <strong class="text-text font-bold">milano.transporte65@gmail.com</strong></span>
</a>
</div>"""

    html = html[:start_idx] + new_content + "\n</div>\n</div>\n</section></main>" + html[end_idx + len(end_tag):]

    with open("c:/Users/Usuario/Downloads/muñoz lp/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("CTA section optimized for mobile successfully.")

if __name__ == "__main__":
    optimize_cta_mobile()
