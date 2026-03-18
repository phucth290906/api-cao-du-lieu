from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI(title="SEO & Metadata Extractor Pro", version="1.0")

@app.get("/")
def home():
    return {"message": "🚀 API is Live and Running 24/7!"}

@app.get("/api/extract")
def extract_seo_data(url: str):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        
        title = soup.title.string if soup.title else "Not Found"
        meta_desc = soup.find("meta", attrs={"name": "description"})
        description = meta_desc["content"] if meta_desc else "Not Found"
        og_image = soup.find("meta", property="og:image")
        image_url = og_image["content"] if og_image else "Not Found"
        
        return {
            "status": "success",
            "original_url": url,
            "metadata": {
                "title": title.strip() if isinstance(title, str) else title,
                "description": description.strip() if isinstance(description, str) else description,
                "thumbnail": image_url
            }
        }
    except Exception as e:
        return {"status": "error", "detail": str(e)}
