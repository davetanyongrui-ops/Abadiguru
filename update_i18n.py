import re
import os

i18n_js = """
const dictionary = {
  "Beranda": { en: "Home", zh: "首页" },
  "Syarat & Ketentuan": { en: "Terms & Conditions", zh: "条款与条件" },
  "Daftarkan Sekarang": { en: "Register Now", zh: "立即注册" },
  "Daftar GOR": { en: "Register GOR", zh: "注册场馆" },
  "Hubungi Kami": { en: "Contact Us", zh: "联系我们" },
  "Abadi Guru - Menangkan Website Booking Lapangan Badminton": { en: "Abadi Guru - Win a Badminton Court Booking Website", zh: "Abadi Guru - 赢取羽毛球馆预订网站" },
  "Syarat & Ketentuan - Abadi Guru": { en: "Terms & Conditions - Abadi Guru", zh: "条款与条件 - Abadi Guru" },
  "Daftarkan Sekarang - Abadi Guru": { en: "Register Now - Abadi Guru", zh: "立即注册 - Abadi Guru" },
  
  "Giveaway Spesial": { en: "Special Giveaway", zh: "特别赠品" },
  "Menangkan Website Booking Lapangan Badminton Senilai": { en: "Win a Badminton Court Booking Website Worth", zh: "赢取价值" },
  "Rp 58.000.000": { en: "Rp 58,000,000", zh: "Rp 58,000,000的羽毛球馆预订网站" },
  "(GRATIS!)": { en: "(FREE!)", zh: "（免费！）" },
  "Tingkatkan kelas GOR Anda. Kami mengundi 1 website eksklusif pada 1 Juni. Berikan pengalaman booking premium untuk pelanggan setia Anda.": { en: "Upgrade your GOR class. We draw 1 exclusive website on June 1st. Provide a premium booking experience for your loyal customers.", zh: "提升您的场馆档次。我们将在6月1日抽取1个独家网站。为您的忠实客户提供优质的预订体验。" },
  "Pelajari Syaratnya": { en: "Learn the Terms", zh: "了解条款" },
  "Lihat Fitur": { en: "View Features", zh: "查看功能" },

  "Bukan Sekadar Website Biasa": { en: "Not Just an Ordinary Website", zh: "不仅仅是一个普通的网站" },
  "Platform premium yang dirancang khusus untuk manajemen Gelanggang Olahraga modern, mengutamakan kemudahan pengelola dan kenyamanan pemain.": { en: "A premium platform specifically designed for modern sports arena management, prioritizing manager convenience and player comfort.", zh: "一个专为现代体育场馆管理设计的优质平台，优先考虑管理者的便利性和玩家的舒适感。" },
  "Ketersediaan Live": { en: "Live Availability", zh: "实时空余情况" },
  "Jadwal lapangan ter-update secara otomatis real-time. Hilangkan risiko double-booking dan kurangi waktu yang terbuang untuk membalas chat ketersediaan jadwal.": { en: "Court schedules are updated automatically in real-time. Eliminate the risk of double scheduling and reduce time wasted replying to availability chats.", zh: "场地时间表实时自动更新。消除重复预订的风险，并减少回复查询空余时间浪费的时间。" },
  "Pembayaran Mudah": { en: "Easy Payment", zh: "便捷支付" },
  "Terintegrasi penuh dengan QRIS dan konfirmasi WhatsApp otomatis. Transaksi lancar tanpa repot cek mutasi manual.": { en: "Fully integrated with QRIS and automatic WhatsApp confirmation. Smooth transactions without the hassle of manual mutation checks.", zh: "与QRIS和WhatsApp自动确认完全集成。交易顺畅，免去手动对账的烦恼。" },
  "Database Pelanggan": { en: "Customer Database", zh: "客户数据库" },
  "Bangun loyalitas. Simpan data pemain dengan rapi dan manfaatkan fitur broadcast untuk promo jam sepi atau info turnamen.": { en: "Build loyalty. Store player data neatly and utilize the broadcast feature for off-peak hour promos or tournament info.", zh: "建立忠诚度。妥善存储玩家数据，并利用广播功能进行闲时促销或比赛信息推送。" },
  "Keunggulan Kompetitif": { en: "Competitive Advantage", zh: "竞争优势" },
  "Tampil modern di mata pemain. Modul manajemen turnamen bawaan membantu Anda menyelenggarakan event dengan profesional dan minim kerumitan.": { en: "Look modern in the eyes of players. The built-in tournament management module helps you organize events professionally with minimal hassle.", zh: "在玩家眼中展现现代化。内置的赛事管理模块帮助您专业地组织活动，减少麻烦。" },

  "Siap untuk Berpartisipasi?": { en: "Ready to Participate?", zh: "准备好参与了吗？" },
  "Pastikan Anda telah memenuhi semua persyaratan di atas. Bergabunglah sekarang untuk mengembangkan fasilitas GOR Anda.": { en: "Ensure you have met all the requirements above. Join now to develop your GOR facility.", zh: "确保您符合上述所有要求。立即加入，发展您的设施。" },
  "Daftar Undian Sekarang": { en: "Register for Giveaway Now", zh: "立即注册参与抽奖" },

  "Mohon baca dengan saksama persyaratan berikut sebelum mendaftarkan GOR Anda dalam program undian.": { en: "Please read the following requirements carefully before registering your GOR in the giveaway program.", zh: "在将您的场馆注册参加抽奖活动前，请仔细阅读以下要求。" },
  "Kualifikasi Peserta": { en: "Participant Qualifications", zh: "参赛资格" },
  "Undian ini terbuka secara eksklusif bagi pemilik, pengelola, atau manajer lapangan bulu tangkis (GOR) yang beroperasi secara aktif di wilayah Republik Indonesia. Peserta wajib mengisi data diri dan data GOR dengan informasi yang valid dan dapat dipertanggungjawabkan. Satu (1) entitas GOR hanya berhak mendaftarkan 1 (satu) entri undian. Pendaftaran ganda untuk GOR yang sama akan didiskualifikasi.": { en: "This giveaway is exclusively open for owners, managers, or directors of active badminton courts in Indonesia. Participants must fill in personal and GOR data with valid and accountable information. Double registration for the same GOR will be disqualified.", zh: "本次抽奖仅限于在印度尼西亚积极运营的羽毛球场的所有者、管理者或负责人。参与者必须提供有效且负责任的信息。同一场馆的重复注册将被取消资格。" },
  "Periode Program": { en: "Program Period", zh: "活动期间" },
  "Pendaftaran undian dibuka sejak halaman ini dipublikasikan dan akan ditutup secara resmi pada tanggal": { en: "Giveaway registration is open from the publication of this page and will officially close on", zh: "抽奖注册自本页面发布起开放，并将于以下日期正式结束：" },
  "31 Mei 2026": { en: "May 31, 2026", zh: "2026年5月31日" },
  "pukul 23:59 WIB.": { en: "at 23:59 WIB.", zh: "晚上 23:59 (WIB)。" },
  "Detail Hadiah": { en: "Prize Details", zh: "奖品详情" },
  "Pemenang utama akan mendapatkan 1 (satu) paket sistem Website Booking Lapangan Badminton terintegrasi (termasuk fitur jadwal live, integrasi WhatsApp, dan sistem QRIS) yang bernilai Rp 58.000.000,-. Hadiah berupa sistem digital dan hak guna, tidak dapat ditukar dengan uang tunai, dialihkan ke pihak lain yang bukan pemilik GOR, atau dikembalikan dalam bentuk apa pun.": { en: "The main winner will receive 1 integrated Badminton Court Booking Website system package worth Rp 58,000,000. Awards cannot be exchanged for cash, transferred to other parties, or returned in any form.", zh: "大奖获得者将赢得1套综合羽毛球场预订网站系统套餐，价值Rp 58,000,000。奖品不得兑换现金，不得转让给其他方，或以任何形式退还。" },
  "PENTING:": { en: "IMPORTANT:", zh: "重要提示：" },
  "Hadiah tidak termasuk biaya pembelian nama domain serta biaya perpanjangan hosting/server tahunan.": { en: "The prize does not include the cost of purchasing a domain name and annual hosting/server renewal fees.", zh: "奖品不包括购买域名的费用及每年的托管/服务器续费。" },
  "Mekanisme Pengundian dan Pengumuman": { en: "Draw and Announcement Mechanism", zh: "抽奖和公告机制" },
  "Pengundian akan dilakukan secara acak, transparan, dan disiarkan secara": { en: "The draw will be done randomly, transparently, and broadcasted", zh: "抽奖将随机、透明地进行，并在此日期直播：" },
  "live": { en: "live", zh: "直播" },
  "pada tanggal": { en: "on the date", zh: "在" },
  "1 Juni 2026": { en: "June 1, 2026", zh: "2026年6月1日" },
  ". Pemenang akan diumumkan melalui platform resmi Abadi Guru dan akan dihubungi secara langsung melalui Nomor WhatsApp yang didaftarkan.": { en: ". The winner will be announced through the official Abadi Guru platform and contacted directly via the registered WhatsApp Number.", zh: "。获胜者将通过官方平台公布，并通过注册的WhatsApp号码直接联系。" },
  "Proses Verifikasi Pemenang": { en: "Winner Verification Process", zh: "获奖者验证流程" },
  "Pemenang yang terpilih wajib melewati proses verifikasi untuk membuktikan keabsahan status sebagai pemilik atau pengelola sah dari GOR yang didaftarkan. Apabila pemenang tidak dapat dihubungi dalam kurun waktu 3x24 jam atau gagal melewati proses verifikasi, penyelenggara berhak membatalkan kemenangan dan mengundi ulang.": { en: "The selected winner must pass a verification process. If the winner cannot be contacted within 3x24 hours or fails the verification process, the organizer reserves the right to cancel the win and redraw.", zh: "选定的获奖者必须通过验证流程。如果获胜者在3x24小时内未联系上或未能通过验证流程，组织者保留取消获奖资格并重新抽奖的权利。" },
  "Ketentuan Lainnya": { en: "Other Terms", zh: "其他条款" },
  "Keikutsertaan dalam program ini 100% GRATIS. Penyelenggara berhak untuk mendiskualifikasi peserta yang terindikasi melakukan kecurangan. Keputusan penyelenggara (Abadi Guru) bersifat mutlak.": { en: "Participation in this program is 100% FREE. The organizer reserves the right to disqualify participants suspected of cheating. The organizer's decision is final.", zh: "参与本项目完全免费。组织者保留取消涉嫌作弊者资格的权利。组织者的决定为最终决定。" },

  "Daftarkan GOR Anda Sekarang!": { en: "Register Your GOR Now!", zh: "立即注册您的场馆！" },
  "Lengkapi Data Berikut": { en: "Complete the Following Data", zh: "填写以下数据" },
  "Nama Lengkap": { en: "Full Name", zh: "全名" },
  "Nama GOR / Fasilitas": { en: "GOR / Facility Name", zh: "场馆 / 设施名称" },
  "Nomor WhatsApp Aktif": { en: "Active WhatsApp Number", zh: "有效的 WhatsApp 号码" },
  "Catatan Tambahan (Opsional)": { en: "Additional Notes (Optional)", zh: "附加说明（可选）" },
  "Kirim Pendaftaran": { en: "Submit Registration", zh: "提交注册" },
  "Tim kami akan menghubungi Anda melalui WhatsApp dalam waktu 1x24 jam.": { en: "Our team will contact you via WhatsApp within 1x24 hours.", zh: "我们的团队将在 24 小时内通过 WhatsApp 与您联系。" },
  
  "Diselenggarakan oleh": { en: "Organized by", zh: "主办方" },
  "Kebijakan Privasi": { en: "Privacy Policy", zh: "隐私政策" },
  "Bantuan": { en: "Help", zh: "帮助" },
  "Kemitraan": { en: "Partnership", zh: "合作" },
  "Sponsored by:": { en: "Sponsored by:", zh: "赞助商：" },
  "© 2024 Abadi Guru Indonesia. Rooted in Sport.": { en: "© 2024 Abadi Guru Indonesia. Rooted in Sport.", zh: "© 2024 Abadi Guru Indonesia. Rooted in Sport." },
};

function changeLanguage(lang) {
  localStorage.setItem('website_lang', lang);
  
  // Update buttons
  document.querySelectorAll('.lang-btn').forEach(btn => {
    if(btn.dataset.lang === lang) {
      btn.classList.add('font-bold', 'text-[#4a7c59]', 'dark:text-[#10B981]');
      btn.classList.remove('text-slate-500', 'font-normal');
    } else {
      btn.classList.remove('font-bold', 'text-[#4a7c59]', 'dark:text-[#10B981]');
      btn.classList.add('text-slate-500', 'font-normal');
    }
  });

  const elements = document.querySelectorAll('h1, h2, h3, h4, h5, h6, p, a, span, label, button, li, strong, em, div, title');
  
  elements.forEach(el => {
    // Only process elements that don't have child elements (or only simple elements)
    Array.from(el.childNodes).forEach(child => {
      if (child.nodeType === 3) { // Text node
        const trimmed = child.nodeValue.trim();
        if(!trimmed) return;
        
        const originalText = child.originalText || trimmed;
        
        if (dictionary[originalText]) {
          if (!child.originalText) child.originalText = originalText;
          
          let newText = originalText;
          if (lang !== 'id') {
             newText = dictionary[originalText][lang] || originalText;
          }
          
          const isStartSpace = child.nodeValue.match(/^\s+/);
          const isEndSpace = child.nodeValue.match(/\s+$/);
          
          let formattedText = newText;
          if (isStartSpace) formattedText = isStartSpace[0] + formattedText;
          if (isEndSpace) formattedText = formattedText + isEndSpace[0];
          
          child.nodeValue = formattedText;
        }
      }
    });

    if (el.placeholder) {
      const originalPlace = el.originalPlaceholder || el.placeholder.trim();
      if (!el.originalPlaceholder) el.originalPlaceholder = originalPlace;
      const dictPlaceholders = {
        "Masukkan nama lengkap Anda": { en: "Enter your full name", zh: "输入您的全名" },
        "Contoh: GOR Jaya Sakti": { en: "Example: GOR Jaya Sakti", zh: "示例：GOR Jaya Sakti" },
        "08xx xxxx xxxx": { en: "12xx xxxx xxxx", zh: "12xx xxxx xxxx" },
        "Informasi tambahan mengenai fasilitas Anda...": { en: "Additional information regarding your facility...", zh: "有关您的设施的附加信息……" }
      };
      if (dictPlaceholders[originalPlace]) {
         el.placeholder = lang === 'id' ? originalPlace : (dictPlaceholders[originalPlace][lang] || originalPlace);
      }
    }
  });
}

document.addEventListener('DOMContentLoaded', () => {
  const savedLang = localStorage.getItem('website_lang') || 'id';
  changeLanguage(savedLang);
});
"""

os.makedirs('assets', exist_ok=True)
with open('assets/i18n.js', 'w') as f:
    f.write(i18n_js)

html_files = ["code.html", "hubungi kami.html", "tos.html"]

lang_switcher_html = """
<div class="flex items-center gap-2 mr-4 bg-[#4a7c59]/5 px-3 py-1.5 rounded-lg border border-[#4a7c59]/20">
    <button onclick="changeLanguage('id')" data-lang="id" class="lang-btn font-bold text-[#4a7c59] dark:text-[#10B981] hover:opacity-80 transition-opacity text-sm">ID</button>
    <span class="text-slate-300 mx-1">|</span>
    <button onclick="changeLanguage('en')" data-lang="en" class="lang-btn text-slate-500 font-normal hover:text-[#4a7c59] transition-colors text-sm">EN</button>
    <span class="text-slate-300 mx-1">|</span>
    <button onclick="changeLanguage('zh')" data-lang="zh" class="lang-btn text-slate-500 font-normal hover:text-[#4a7c59] transition-colors text-sm">ZH</button>
</div>
"""

for file_name in html_files:
    try:
        with open(file_name, 'r') as f:
            content = f.read()

        # Add script to head or before closing tag
        if '<script src="assets/i18n.js"></script>' not in content:
            content = content.replace("</body>", '<script src="assets/i18n.js"></script>\n</body>')
        
        # Inject switcher just before the "Daftar GOR" button/div
        # Find where the Trailing Action starts
        if '<!-- Trailing Action -->' in content and 'lang-btn' not in content:
            content = re.sub(r'(<!-- Trailing Action -->\s*<div[^>]*>)', r'\1\n' + lang_switcher_html, content)
            
        with open(file_name, 'w') as f:
            f.write(content)
            
        print(f"Updated {file_name}")
    except Exception as e:
        print(f"Failed {file_name}: {e}")
