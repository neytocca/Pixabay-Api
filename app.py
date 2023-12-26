# app.py

import requests

PIXABAY_API_KEY = "41149428-b8bb084549fa840c5de8225d9"
PIXABAY_API_URL = "https://pixabay.com/api/"

def search_images(sorgu, renkler=None, kategoriler=None, yetişkin_içerik=False):
    if not sorgu:
        print("Hata: Boş bir arama sorgusu gönderilemez.")
        return None

    valid_colors = ["gri tonları", "transparan", "kırmızı", "turuncu", "sarı", "yeşil", "turkuaz", "mavi", "leylak", "pembe", "beyaz", "gri", "siyah", "kahverengi"]

    valid_categories = ["moda", "doğa", "arka_plan", "bilim", "eğitim", "insanlar", "duygular",
                        "sağlık", "mekanlar", "hayvanlar", "endüstri", "yiyecek", "bilgisayar", "spor", "taşımacılık",
                        "seyahat", "binalar", "iş", "müzik"]

    if renkler and not all(renk in valid_colors for renk in renkler):
        print(f"Hata: Geçersiz renk değeri. Kabul edilen renk değerleri: {', '.join(valid_colors)}")
        return None

    if kategoriler and not all(kategori in valid_categories for kategori in kategoriler):
        print(f"Hata: Geçersiz kategori değeri. Kabul edilen kategori değerleri: {', '.join(valid_categories)}")
        return None

    params = {
        "key": PIXABAY_API_KEY,
        "q": sorgu,
        "colors": ",".join(renkler) if renkler else None,
        "category": ",".join(kategoriler) if kategoriler else None,
        "safesearch": not yetişkin_içerik
    }

    response = requests.get(PIXABAY_API_URL, params=params)

    try:
        data = response.json()
        if "hits" in data:
            return data["hits"]
        else:
            print(f"Uyarı: '{sorgu}' kelimesine ait bir görsel bulunamadı.")
            return None
    except Exception as e:
        print(f"JSON decode hatası: {e}")
        return None

def download_image(url, filename):
    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

    print(f"{filename} başarıyla indirildi.")
