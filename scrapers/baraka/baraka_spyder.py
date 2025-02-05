import httpx
from bs4 import BeautifulSoup
from typing import List, Dict, Any, Optional
import asyncio
import logging
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("BarakaSpyder")
CONCURRENT_REQUESTS = 10

class BarakaSpyder:
    def __init__(self):
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
        }
        self.semaphore = asyncio.Semaphore(CONCURRENT_REQUESTS)

    async def fetch_page(self, client, page):
        try:
            url = f"https://barakacomputer.net/page/{page}/?s={self.search_term}&post_type=product"
            
            response = await client.get(url, headers=self.headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            product_cards = soup.select('li.product-warp-item')
            products = []
            for card in product_cards:
                try:
                    name = card.select_one('a.name').text.strip()
                    original_price_element = card.select_one('span.price del span.woocommerce-Price-amount')
                    original_price = original_price_element.text.strip() if original_price_element else None
                    current_price_element = card.select_one('span.price ins span.woocommerce-Price-amount')
                    current_price = current_price_element.text.strip() if current_price_element else None
                    product_url = card.select_one('a.product-img')['href']
                    image_url = card.select_one('div.main-img img')['src']
                    products.append({
                        'name': name,
                        'original_price': original_price,
                        'current_price': current_price,
                        'product_url': product_url,
                        'image_url': image_url
                    })
                except Exception:
                    continue
            logger.info(f"Found {len(products)} products on page {page}.")
            return products
        except Exception as e:
            logger.error(f"Error fetching page {page}: {str(e)}")
            return []

    async def scrap(self, search_term) -> List[Dict[str, Any]]:
        """Scrape products concurrently."""
        self.search_term = search_term
        timeout = httpx.Timeout(30.0, connect=10.0)
        limits = httpx.Limits(max_connections=CONCURRENT_REQUESTS, max_keepalive_connections=20)
        async with httpx.AsyncClient(timeout=timeout, limits=limits) as client:
            tasks = [self.fetch_page(client, page) for page in range(1, 11)]
            all_results = await asyncio.gather(*tasks)
        # Flatten and filter results
        products = [product for result in all_results if result for product in result]
        logger.info(f"Found {len(products)} products in total.")
        return products

# Example usage
if __name__ == "__main__":
    spyder = BarakaSpyder()
    search_term = "rtx"
    results = asyncio.run(spyder.scrap(search_term))
    with open("baraka_results.json", "w", encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
    print("Results have been written to baraka_results.json")