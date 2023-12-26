# main.py

import streamlit as st
from app import search_images, download_image

def main():
    st.title("Pixabay Görsel Arama Platformu")
    search_query = st.text_input("Görsel Ara")

    renkler = st.multiselect("Renk Filtreleme",
                            ["gri tonları", "transparan", "kırmızı", "turuncu", "sarı", "yeşil", "turkuaz", "mavi",
                             "leylak", "pembe", "beyaz", "gri", "siyah", "kahverengi"])

    kategoriler = st.multiselect("Kategori Filtreleme",
                                ["moda", "doğa", "arka_plan", "bilim", "eğitim", "insanlar", "duygular",
                                 "sağlık", "mekanlar", "hayvanlar", "endüstri", "yiyecek", "bilgisayar", "spor", "taşımacılık",
                                 "seyahat", "binalar", "iş", "müzik"])

    yetişkin_içerik = st.checkbox("Yetişkin İçerikleri Göster")

    if st.button("Ara"):
        görseller = search_images(search_query, renkler, kategoriler, yetişkin_içerik)
        if görseller is None:
            st.error("Görsel arama sırasında bir hata oluştu. Lütfen tekrar deneyin.")
        elif not görseller:
            st.warning(f"'{search_query}' kelimesine ait bir görsel bulunamadı.")
        else:
            display_images(görseller)

def display_images(görseller):
    for index, görsel in enumerate(görseller):
        st.image(görsel["webformatURL"], caption=görsel["tags"], use_column_width=True)

        # Her bir görsel için bir download button oluştur
        download_button = st.button(
            label=f"Görseli İndir ({görsel['tags']})",
            key=f"download_button_{index}",  # Benzersiz bir key ekleniyor
            help=f"{görsel['tags']} görselini indir"
        )

        # Eğer download buttona basılırsa, download_image fonksiyonunu çağır
        if download_button:
            download_image(görsel["webformatURL"], f"{görsel['tags']}_{index}.jpg")

if __name__ == "__main__":
    main()
