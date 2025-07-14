import streamlit as st

st.set_page_config(page_title="Keripik Pisang Mas Boy", page_icon="🍌", layout="centered")

# --- Header ---
st.title("🍌 Keripik Pisang Mas Boy")
st.subheader("Renyahnya Bikin Nagih, Rasanya Beda dari yang Lain!")
st.write("""
Keripik Pisang Mas Boy adalah usaha camilan rumahan yang menyajikan keripik pisang renyah dengan cita rasa kekinian.

Tersedia dalam tiga varian rasa favorit: **Matcha**, **Tiramisu**, dan **Coklat**.

Keripik Pisang Mas Boy dibuat dari pisang pilihan dan diolah secara higienis tanpa bahan pengawet.
Cocok untuk teman santai, oleh-oleh, atau camilan harian.
""")

# --- Harga ---
st.success("📦 Harga per pack hanya Rp 15.000,-")

# --- Gambar Produk ---
st.header("📸 Varian Rasa")

col1, col2 = st.columns(2)

with col1:
    st.image("images/coklat.jpg", caption="Coklat", use_column_width=True)
    st.image("images/matcha.jpg", caption="Matcha", use_column_width=True)

with col2:
    st.image("images/tiramisu.jpg", caption="Tiramisu", use_column_width=True)
    st.image("images/paket.jpg", caption="Paket Keripik Pisang Mas Boy", use_column_width=True)

# --- Tombol Pemesanan ---
st.markdown("### 📲 Pesan Sekarang")
st.markdown("""
Klik tombol di bawah untuk memesan langsung via WhatsApp:

[💬 Pesan via WhatsApp](https://wa.me/6282231305330?text=Halo%2C%20saya%20ingin%20pesan%20Keripik%20Pisang%20Mas%20Boy%20ya.%20Tolong%20infonya.%20Terima%20kasih!)  
""")

# --- Footer ---
st.markdown("---")
st.caption("Usaha rumahan oleh Mas Boy 🍌 | Instagram: @keripikmasboy (jika ada)")
