import re

files = ["code.html", "hubungi kami.html", "tos.html"]
all_texts = set()

def extract_text(html):
    # Remove scripts and styles
    html = re.sub(r'<script.*?</script>', '', html, flags=re.DOTALL)
    html = re.sub(r'<style.*?</style>', '', html, flags=re.DOTALL)
    # Remove HTML tags
    # We want to keep text between tags
    texts = re.findall(r'>([^<]+)<', html)
    for t in texts:
        t = t.strip()
        # Clean up HTML entities
        t = t.replace('&amp;', '&')
        if len(t) > 2 and not t.isnumeric():
            all_texts.add(t)

for f in files:
    try:
        with open(f, 'r') as file:
            extract_text(file.read())
    except:
        pass

for i, t in enumerate(sorted(all_texts)):
    print(f"{i}: {t}")

