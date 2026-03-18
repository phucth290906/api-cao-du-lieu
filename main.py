from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI(title="API Trích Xuất Dữ Liệu SEO", version="1.0")

@app.get("/")
def trang_chu():
    return {"Thong_diep": "🚀 API Của Kỹ Sư Trưởng Đang Chạy Trên Cloud 24/7!"}

@app.get("/api/extract")
def extract_seo_data(url: str):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        
        title = soup.title.string if soup.title else "Không tìm thấy"
        meta_desc = soup.find("meta", attrs={"name": "description"})
        description = meta_desc["content"] if meta_desc else "Không tìm thấy"
        og_image = soup.find("meta", property="og:image")
        image_url = og_image["content"] if og_image else "Không tìm thấy"
        
        return {
            "trang_thai": "Thành công",
            "url_goc": url,
            "du_lieu": {
                "tieu_de": title.strip() if isinstance(title, str) else title,
                "mo_ta": description.strip() if isinstance(description, str) else description,
                "link_anh_bia": image_url
            }
        }
    except Exception as e:
        return {"trang_thai": "Lỗi", "chi_tiet": str(e)}
