import re

files = ['code.html', 'tos.html', 'hubungi kami.html']

for f in files:
    with open(f, 'r') as file:
        content = file.read()
    
    # 1. Title replacement
    content = content.replace("Terra GOR", "Abadi Guru")

    # 2. Main Logo replacement in Navbars
    # We look for <a ...>Abadi Guru</a> pattern roughly
    # code.html:
    # <a class="font-['Literata'] text-2xl font-bold text-[#4a7c59] tracking-tight" href="code.html">
    #            Abadi Guru
    #        </a>
    
    abadi_guru_logo_html = """
<a class="flex items-center gap-2 group" href="code.html">
    <div class="w-9 h-9 rounded-xl bg-[#4a7c59]/10 flex items-center justify-center group-hover:bg-[#4a7c59]/20 transition-colors">
        <span class="material-symbols-outlined text-[#4a7c59]" style="font-size: 20px;">emoji_events</span>
    </div>
    <span class="font-['Literata'] font-bold text-2xl tracking-tight text-[#2e3230] dark:text-white">
        Abadi<span class="text-[#4a7c59] dark:text-[#10B981]">Guru</span>
    </span>
</a>
"""

    # In code.html
    content = re.sub(r'<a[^>]*font-\[\'Literata\'\][^>]*>[^<]*Abadi Guru[^<]*</a>', abadi_guru_logo_html.strip(), content)

    # In hubungi kami.html it might be <a href="code.html" class="font-['Literata'] ...">Abadi Guru</a>
    # We already caught it above hopefully. Let's do another pass if needed.
    # Wait, hubungi kami is: <a href="code.html" class="font-['Literata'] text-2xl font-bold text-[#4a7c59] dark:text-[#10B981]">Abadi Guru</a>
    content = re.sub(r'<a[^>]*>Abadi Guru</a>', abadi_guru_logo_html.strip(), content)
    # also <div class="font-['Literata'] text-lg font-semibold text-[#4a7c59]">Abadi Guru</div> in footer
    footer_logo_html = """
<div class="flex items-center gap-2">
    <div class="w-7 h-7 rounded-lg bg-[#4a7c59]/10 flex items-center justify-center">
        <span class="material-symbols-outlined text-[#4a7c59]" style="font-size: 16px;">emoji_events</span>
    </div>
    <span class="font-['Literata'] font-bold text-lg tracking-tight text-[#2e3230] dark:text-white">
        Abadi<span class="text-[#4a7c59] dark:text-[#10B981]">Guru</span>
    </span>
</div>
"""
    content = re.sub(r'<div class="font-\[\'Literata\'\][^>]*>[^<]*Abadi Guru[^<]*</div>', footer_logo_html.strip(), content)
    content = re.sub(r'<span class="font-\[\'Literata\'\][^>]*>[^<]*Abadi Guru[^<]*</span>', footer_logo_html.strip(), content)

    # 3. Add sponsored by into footer
    # Find "© 2024 Abadi Guru Indonesia" and inject sponsor HTML right before or within its container
    sponsor_html = """
<div class="flex flex-col md:flex-row items-center gap-4 mt-6 mb-2">
    <span class="text-xs text-slate-500 uppercase tracking-widest font-['Nunito_Sans']">Sponsored by:</span>
    <img src="assets/alfa_logo.png" alt="Alfa Learning Online" class="h-10 object-contain" />
</div>
"""
    if "Sponsored by:" not in content:
        content = content.replace("© 2024 Abadi Guru Indonesia", sponsor_html + "© 2024 Abadi Guru Indonesia")

    with open(f, 'w') as file:
        file.write(content)

print("Updates applied.")
