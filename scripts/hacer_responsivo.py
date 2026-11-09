import re

def make_responsive():
    with open("c:/Users/Usuario/Downloads/muñoz lp/index.html", "r", encoding="utf-8") as f:
        html = f.read()

    # Pattern for section 5 (Planifica tu viaje)
    sec5_pattern = r'<!-- 5\. Brand OS -->\s*<section class="py-\[120px\] px-margin max-w-\[1728px\] mx-auto bg-page-bg">.*?<!-- 6\. Lumio Studio -->'
    
    new_sec5 = """<!-- 5. Brand OS -->
<section class="py-12 sm:py-16 md:py-[120px] px-4 sm:px-6 md:px-margin max-w-[1728px] mx-auto bg-page-bg">
<div class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-[100px] items-center">
<div class="bg-gradient-to-br from-soft-card-2 to-soft-card rounded-3xl lg:rounded-[40px] p-3.5 sm:p-6 lg:p-8 min-h-[460px] sm:min-h-[540px] lg:h-[700px] flex items-center justify-center relative overflow-hidden border border-line/30 shadow-sm w-full">
<div class="w-full max-w-md bg-white-card rounded-2xl shadow-xl border border-line/20 p-4 sm:p-6"><div class="flex items-center justify-between mb-5 sm:mb-8"><span class="font-label font-bold text-sm text-text">Planifica tu viaje</span><span class="material-symbols-outlined text-muted text-xl sm:text-2xl">directions_car</span></div><div class="space-y-2.5 sm:space-y-4"><div class="flex items-center gap-3 sm:gap-4 p-2.5 sm:p-3 hover:bg-soft-card rounded-xl transition-colors"><span class="material-symbols-outlined text-[#FF4B2B] shrink-0 text-xl sm:text-2xl">trip_origin</span><div class="min-w-0 flex-1"><p class="font-label text-[9px] sm:text-[10px] text-muted uppercase tracking-wider font-semibold">Origen</p><p class="font-body-md text-xs sm:text-[15px] font-medium text-text leading-snug break-words">Hotel Ritz-Carlton / Vitacura</p></div></div><div class="flex items-center gap-3 sm:gap-4 p-2.5 sm:p-3 hover:bg-soft-card rounded-xl transition-colors"><span class="material-symbols-outlined text-[#8A2387] shrink-0 text-xl sm:text-2xl">location_on</span><div class="min-w-0 flex-1"><p class="font-label text-[9px] sm:text-[10px] text-muted uppercase tracking-wider font-semibold">Destino</p><p class="font-body-md text-xs sm:text-[15px] font-medium text-text leading-snug break-words">Aeropuerto Internacional SCL (T2)</p></div></div><div class="flex items-center gap-3 sm:gap-4 p-2.5 sm:p-3 hover:bg-soft-card rounded-xl transition-colors"><span class="material-symbols-outlined text-[#E94057] shrink-0 text-xl sm:text-2xl">airport_shuttle</span><div class="min-w-0 flex-1"><p class="font-label text-[9px] sm:text-[10px] text-muted uppercase tracking-wider font-semibold">Vehículo Seleccionado</p><p class="font-body-md text-xs sm:text-[15px] font-medium text-text leading-snug break-words">Sedán Ejecutivo Nissan Versa</p></div></div><div class="flex items-center gap-3 sm:gap-4 p-2.5 sm:p-3 hover:bg-soft-card rounded-xl transition-colors"><span class="material-symbols-outlined text-[#F27121] shrink-0 text-xl sm:text-2xl">schedule</span><div class="min-w-0 flex-1"><p class="font-label text-[9px] sm:text-[10px] text-muted uppercase tracking-wider font-semibold">Horario y Tarifa</p><p class="font-body-md text-xs sm:text-[15px] font-medium text-text leading-snug break-words">Inmediata • Tarifa fija garantizada</p></div></div></div></div>
</div>
<div class="flex flex-col justify-center h-full max-w-lg"><h3 class="font-display text-2xl sm:text-h2 mb-6 sm:mb-12 font-bold tracking-tight text-text">La garantía de un viaje sin contratiempos.</h3><div class="relative pl-6 sm:pl-8 border-l-[3px] border-line space-y-8 sm:space-y-12"><div class="absolute left-[-3px] top-0 w-[3px] h-1/3 bg-gradient-to-b from-[#FF416C] to-[#FF4B2B]"></div><div><h4 class="font-h3 text-lg sm:text-xl font-bold mb-2 sm:mb-3 text-text">Puntualidad Rigurosa</h4><p class="font-body-md text-sm sm:text-base text-muted leading-relaxed">Llegamos 15 minutos antes de la hora acordada para que tu itinerario comience con total serenidad.</p></div><div class="opacity-50 hover:opacity-100 transition-opacity"><h4 class="font-h3 text-lg sm:text-xl font-bold mb-2 sm:mb-3 text-text">Monitoreo en Tiempo Real</h4><p class="font-body-md text-sm sm:text-base text-muted leading-relaxed">Seguimiento constante de vuelos y tráfico metropolitano para optimizar las rutas más veloces y seguras.</p></div><div class="opacity-50 hover:opacity-100 transition-opacity"><h4 class="font-h3 text-lg sm:text-xl font-bold mb-2 sm:mb-3 text-text">Tarifas Transparentes</h4><p class="font-body-md text-sm sm:text-base text-muted leading-relaxed">Precios fijos sin sorpresas ni recargos ocultos, con facturación electrónica inmediata para empresas.</p></div></div></div>
</div>
</section>
<!-- 6. Lumio Studio -->"""

    html = re.sub(sec5_pattern, new_sec5, html, flags=re.DOTALL)

    # Also update section 6 (Concierge) for consistent responsive display
    sec6_pattern = r'<!-- 6\. Lumio Studio -->\s*<section class="py-\[120px\] px-margin max-w-\[1728px\] mx-auto bg-page-bg">.*?<!-- 7\. Team Use Cases -->'
    new_sec6 = """<!-- 6. Lumio Studio -->
<section class="py-12 sm:py-16 md:py-[120px] px-4 sm:px-6 md:px-margin max-w-[1728px] mx-auto bg-page-bg">
<div class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-[100px] items-center">
<div class="flex flex-col justify-center h-full max-w-lg order-2 lg:order-1"><h3 class="font-display text-2xl sm:text-h2 mb-6 sm:mb-12 font-bold tracking-tight text-text">Soluciones de movilidad a tu medida.</h3><div class="relative pl-6 sm:pl-8 border-l-[3px] border-line space-y-8 sm:space-y-10"><div class="absolute left-[-3px] top-0 w-[3px] h-1/4 bg-gradient-to-b from-[#FF416C] to-[#FF4B2B]"></div><div><h4 class="font-h3 text-lg sm:text-xl font-bold mb-2 text-text">Atención Corporativa y Convenios</h4><p class="font-body-md text-sm sm:text-base text-muted leading-relaxed">Cuentas corrientes para empresas, reportes mensuales y soporte dedicado 24/7.</p></div><div class="opacity-60 hover:opacity-100 transition-opacity"><h4 class="font-h3 text-lg sm:text-xl font-bold mb-2 text-text">Recepción VIP en Aeropuerto</h4><p class="font-body-md text-sm sm:text-base text-muted leading-relaxed">Bienvenida personalizada con letrero digital y asistencia con equipaje hasta el vehículo.</p></div><div class="opacity-60 hover:opacity-100 transition-opacity"><h4 class="font-h3 text-lg sm:text-xl font-bold mb-2 text-text">Flota Diversificada</h4><p class="font-body-md text-sm sm:text-base text-muted leading-relaxed">Desde sedanes ejecutivos hasta vans de alta capacidad para delegaciones y familias.</p></div><div class="opacity-60 hover:opacity-100 transition-opacity"><h4 class="font-h3 text-xl font-bold mb-2 text-text">Conductores Calificados</h4><p class="font-body-md text-sm sm:text-base text-muted leading-relaxed">Profesionales con amplia trayectoria, vestimenta formal y dominio de idiomas para extranjeros.</p></div></div></div>
<div class="bg-gradient-to-tr from-[#E0EAFC] to-[#CFDEF3] rounded-3xl lg:rounded-[40px] p-4 sm:p-6 lg:p-8 min-h-[380px] sm:min-h-[460px] lg:h-[700px] flex items-center justify-center relative overflow-hidden border border-line/30 shadow-inner order-1 lg:order-2 w-full">
<div class="w-full max-w-lg bg-white/80 backdrop-blur-xl rounded-2xl sm:rounded-3xl shadow-2xl p-5 sm:p-8 border border-white/50"><div class="flex items-center gap-3 mb-5 sm:mb-6"><img src="logo.png" alt="Milano" class="w-[26px] h-[26px] rounded-full object-cover shrink-0"><span class="font-label text-xs font-bold text-muted">MILANO CONCIERGE</span></div><div class="bg-white/60 backdrop-blur-md rounded-xl p-3.5 sm:p-4 mb-5 sm:mb-6 border border-white/50 shadow-sm"><p class="font-body-md text-xs sm:text-[15px] text-text">"Necesito un sedán ejecutivo en Hotel Mandarin a las 07:30 hrs con destino al Aeropuerto SCL, vuelo internacional."</p></div><div class="flex justify-end"><div class="w-8 h-8 rounded-full bg-gradient-to-r from-[#FF416C] to-[#FF4B2B] flex items-center justify-center shadow-md animate-pulse"><span class="material-symbols-outlined text-white text-sm">check_circle</span></div></div></div>
</div>
</div>
</section>
<!-- 7. Team Use Cases -->"""

    html = re.sub(sec6_pattern, new_sec6, html, flags=re.DOTALL)

    with open("c:/Users/Usuario/Downloads/muñoz lp/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Mobile responsiveness updated successfully.")

if __name__ == "__main__":
    make_responsive()
