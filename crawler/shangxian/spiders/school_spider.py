import scrapy
from bs4 import BeautifulSoup
import json
import os

class SchoolSpider(scrapy.Spider):
    name = "school"
    start_urls = [
        # 待添加学校官网URL
    ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.output_dir = "./data/raw"
        os.makedirs(self.output_dir, exist_ok=True)
    
    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else ""
        content = soup.get_text(separator="\n", strip=True)
        
        data = {
            "url": response.url,
            "title": title,
            "content": content,
            "source": "school_website"
        }
        
        filename = f"{self.output_dir}/{hash(response.url)}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        yield data
        
        for next_page in response.css('a::attr(href)'):
            yield response.follow(next_page, self.parse)
