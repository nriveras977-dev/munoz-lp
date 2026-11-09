import re

def update_brand_and_header():
    with open("c:/Users/Usuario/Downloads/muñoz lp/index.html", "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update Title
    html = re.sub(
        r"<title>.*?</title>",
        "<title>Transportes Milano - Transporte Ejecutivo, Taxis y Arriendo de Vehículos</title>",
        html,
        count=1
    )

    # 2. Update Header: Place logo in the center
    old_header_pattern = r"<!-- 1\. Floating Nav \(TopAppBar\) -->\s*<header.*?</header>"
    new_header = """<!-- 1. Floating Nav (TopAppBar) -->
<header class="fixed top-[20px] left-0 right-0 z-50 flex items-center justify-center px-4 w-full pointer-events-none">
<div class="pointer-events-auto w-full max-w-[860px] flex items-center justify-between bg-[#000000]/95 backdrop-blur-xl rounded-full px-5 py-2 shadow-2xl border border-white/10 h-[64px] relative">
<div class="flex items-center gap-6"><span class="text-page-bg font-bold tracking-tight text-xs md:hidden uppercase">Transportes Milano</span><nav class="hidden md:flex items-center gap-6"><a class="font-label text-xs uppercase tracking-wider text-page-bg/80 hover:text-page-bg transition-colors duration-300" href="#servicios">Servicios</a><a class="font-label text-xs uppercase tracking-wider text-page-bg/80 hover:text-page-bg transition-colors duration-300" href="#aeropuerto">Aeropuerto</a><a class="font-label text-xs uppercase tracking-wider text-page-bg/80 hover:text-page-bg transition-colors duration-300" href="#hoteles">Hoteles</a></nav></div>
<div class="absolute left-1/2 -translate-x-1/2 flex items-center justify-center"><a class="flex items-center justify-center group" href="#" title="Transportes Milano"><img alt="Logo Transportes Milano" class="h-12 w-12 rounded-full object-cover shadow-lg group-hover:scale-110 transition-transform duration-300" src="logo.png"></a></div>
<div class="flex items-center gap-5"><nav class="hidden md:flex items-center gap-6"><a class="font-label text-xs uppercase tracking-wider text-page-bg/80 hover:text-page-bg transition-colors duration-300" href="#arriendo">Arriendo</a><a class="font-label text-xs uppercase tracking-wider text-page-bg/80 hover:text-page-bg transition-colors duration-300" href="#contacto">Contacto</a></nav><button class="font-label rounded-full hover:bg-page-bg hover:text-black transition-all duration-300 shrink-0 flex items-center px-4 text-[10px] h-[34px] font-semibold uppercase tracking-wider bg-surface-container-low text-primary-container" onclick="document.getElementById('whatsapp-quote-modal').classList.remove('hidden')">Reservar taxi</button></div>
</div>
</header>"""
    html = re.sub(old_header_pattern, new_header, html, flags=re.DOTALL)

    # 3. Update Hero image alt text
    html = re.sub(r'alt="Servicio Ejecutivo de Transporte.*?"', 'alt="Servicio Ejecutivo - Transportes Milano"', html)

    # 4. Concierge badge
    old_concierge = r'<div class="w-\[24px\] h-\[24px\] rounded-full border border-black flex items-center justify-center shrink-0"><span class="text-black font-bold text-\[10px\] leading-none">M</span></div><span class="font-label text-xs font-bold text-muted">.*?CONCIERGE</span>'
    new_concierge = '<img src="logo.png" alt="Milano" class="w-[26px] h-[26px] rounded-full object-cover shrink-0"><span class="font-label text-xs font-bold text-muted">MILANO CONCIERGE</span>'
    html = re.sub(old_concierge, new_concierge, html)

    # 5. Testimonial quote
    html = re.sub(
        r'"Muñoz nos entrega la tranquilidad',
        '"Transportes Milano nos entrega la tranquilidad',
        html
    )

    # 6. Call to Action headline and badge before footer
    old_cta_badge = r'<div class="w-12 h-12 rounded-full border border-text flex items-center justify-center mb-12">\s*<span class="text-text font-bold text-xl leading-none">M</span>\s*</div>'
    new_cta_badge = '<img src="logo.png" alt="Transportes Milano" class="w-20 h-20 rounded-full object-cover shadow-xl mb-8">'
    html = re.sub(old_cta_badge, new_cta_badge, html)

    html = re.sub(
        r'Experimenta la comodidad de viajar con Muñoz',
        'Experimenta la comodidad de viajar con Transportes Milano',
        html
    )

    # 7. Footer brand and logo
    old_footer_brand = r'<div class="flex items-center gap-3"><div class="w-10 h-10 rounded-full border border-white/20 flex items-center justify-center shrink-0"><span class="text-white font-bold text-lg leading-none">M</span></div><span class="text-white font-bold tracking-tight text-lg">.*?</span></div>'
    new_footer_brand = '<div class="flex items-center gap-3"><img src="logo.png" alt="Transportes Milano" class="w-10 h-10 rounded-full object-cover border border-white/20 shrink-0"><span class="text-white font-bold tracking-tight text-lg">TRANSPORTES MILANO</span></div>'
    html = re.sub(old_footer_brand, new_footer_brand, html)

    html = re.sub(r'>Sobre Muñoz<', '>Sobre Transportes Milano<', html)
    html = re.sub(
        r'© 2025 Muñoz Transporte y Arriendo de Vehículos',
        '© 2025 Transportes Milano',
        html
    )

    # 8. WhatsApp Modal & submit message
    old_modal_logo = r'<div class="w-9 h-9 rounded-full bg-white/10 border border-white/20 flex items-center justify-center shrink-0"><span class="text-white font-bold text-sm leading-none">M</span></div>'
    new_modal_logo = '<img src="logo.png" alt="Milano" class="w-9 h-9 rounded-full object-cover border border-white/20 shrink-0">'
    html = re.sub(old_modal_logo, new_modal_logo, html)

    html = re.sub(
        r'¡Hola Muñoz Transporte!',
        '¡Hola Transportes Milano!',
        html
    )

    with open("c:/Users/Usuario/Downloads/muñoz lp/index.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("index.html updated successfully with Transportes Milano and centered logo.")

if __name__ == "__main__":
    update_brand_and_header()
