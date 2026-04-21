import re
import os

files = ["code.html", "hubungi kami.html", "tos.html"]

nav_target = """<a class="flex items-center gap-2 group" href="code.html">
    <div class="w-9 h-9 rounded-xl bg-[#4a7c59]/10 flex items-center justify-center group-hover:bg-[#4a7c59]/20 transition-colors">
        <span class="material-symbols-outlined text-[#4a7c59]" style="font-size: 20px;">emoji_events</span>
    </div>
    <span class="font-['Literata'] font-bold text-2xl tracking-tight text-[#2e3230] dark:text-white">
        Abadi<span class="text-[#4a7c59] dark:text-[#10B981]">Guru</span>
    </span>
</a>"""

nav_replacement = """<a class="flex items-center gap-2 group" href="code.html">
    <img src="assets/abadiguru_logo_BT.png" alt="Abadi Guru Logo" class="h-10 dark:hidden" />
    <img src="assets/abadiguru_logo_WT.png" alt="Abadi Guru Logo" class="hidden dark:block h-10" />
</a>"""


footer_target = """<div class="flex items-center gap-2">
    <div class="w-7 h-7 rounded-lg bg-[#4a7c59]/10 flex items-center justify-center">
        <span class="material-symbols-outlined text-[#4a7c59]" style="font-size: 16px;">emoji_events</span>
    </div>
    <span class="font-['Literata'] font-bold text-lg tracking-tight text-[#2e3230] dark:text-white">
        Abadi<span class="text-[#4a7c59] dark:text-[#10B981]">Guru</span>
    </span>
</div>"""

footer_replacement = """<div class="flex items-center gap-2">
    <img src="assets/abadiguru_logo_BT.png" alt="Abadi Guru Logo" class="h-10 dark:hidden opacity-90" />
    <img src="assets/abadiguru_logo_WT.png" alt="Abadi Guru Logo" class="hidden dark:block h-10 opacity-90" />
</div>"""

for file_name in files:
    try:
        with open(file_name, 'r') as f:
            content = f.read()

        # Update Nav
        content = content.replace(nav_target, nav_replacement)
        # Update Footer
        content = content.replace(footer_target, footer_replacement)
        
        # Make alfa learning bigger
        content = content.replace('class="h-10 object-contain"', 'class="h-16 md:h-20 object-contain"')

        with open(file_name, 'w') as f:
            f.write(content)
            
        print(f"Updated {file_name}")
    except Exception as e:
        print(f"Failed {file_name}: {e}")
