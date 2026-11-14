def add_contact_info():
    with open("c:/Users/Usuario/Downloads/muñoz lp/index.html", "r", encoding="utf-8") as f:
        html = f.read()

    target_cta = '<div class="flex flex-col sm:flex-row gap-6"><button class="bg-transparent border border-text/30 text-text font-label rounded-full hover:bg-text hover:text-white transition-all duration-300 shrink-0 flex items-center px-6 text-[10px] h-[40px] font-bold uppercase tracking-wider" onclick="document.getElementById(\'whatsapp-quote-modal\').classList.remove(\'hidden\')">Cotizar traslado</button><button class="bg-black text-white font-label rounded-full hover:bg-gray-800 transition-all duration-300 shrink-0 flex items-center px-6 text-[10px] h-[40px] font-bold uppercase tracking-wider shadow-sm">Llamar ahora</button></div>'

    new_cta = """<div class="flex flex-col sm:flex-row gap-6">
<button class="bg-transparent border border-text/30 text-text font-label rounded-full hover:bg-text hover:text-white transition-all duration-300 shrink-0 flex items-center justify-center px-6 text-[10px] h-[40px] font-bold uppercase tracking-wider" onclick="document.getElementById('whatsapp-quote-modal').classList.remove('hidden')">Cotizar traslado</button>
<a href="tel:+56935944255" class="bg-black text-white font-label rounded-full hover:bg-gray-800 transition-all duration-300 shrink-0 flex items-center justify-center px-6 text-[10px] h-[40px] font-bold uppercase tracking-wider shadow-sm">Llamar ahora</a>
</div>
<div class="flex flex-col sm:flex-row items-center justify-center gap-3 sm:gap-8 mt-8 text-text/80 font-body-md text-sm sm:text-base">
<a href="tel:+56935944255" class="flex items-center gap-2 hover:text-black transition-colors font-medium">
<span class="material-symbols-outlined text-[#FF4B2B] text-xl">call</span>
<span>Número: <strong class="text-text font-bold">935 944 255</strong></span>
</a>
<span class="hidden sm:inline-block text-line font-bold">•</span>
<a href="mailto:milano.transporte65@gmail.com" class="flex items-center gap-2 hover:text-black transition-colors font-medium">
<span class="material-symbols-outlined text-[#8A2387] text-xl">mail</span>
<span>Correo: <strong class="text-text font-bold">milano.transporte65@gmail.com</strong></span>
</a>
</div>"""

    if target_cta not in html:
        raise ValueError("Target CTA string not found!")

    html = html.replace(target_cta, new_cta, 1)

    # Actualizar número real en modal/widget de WhatsApp
    html = html.replace("56912345678", "56935944255")

    # Actualizar enlaces de teléfono y correo en el footer
    html = html.replace('href="#"><span class="material-symbols-outlined text-[20px]">call</span></a>', 'href="tel:+56935944255"><span class="material-symbols-outlined text-[20px]">call</span></a>')
    html = html.replace('href="#"><span class="material-symbols-outlined text-[20px]">mail</span></a>', 'href="mailto:milano.transporte65@gmail.com"><span class="material-symbols-outlined text-[20px]">mail</span></a>')

    with open("c:/Users/Usuario/Downloads/muñoz lp/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Contact info added successfully.")

if __name__ == "__main__":
    add_contact_info()
