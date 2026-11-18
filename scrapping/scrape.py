import requests
import time
from bs4 import BeautifulSoup
from config.db_config import get_db_connection

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/116.0.0.0 Safari/537.36"
}

cities = {
   
    
    
    "bhopal": "Bhopal",
    "lucknow": "Lucknow",
    "kanpur": "Kanpur",
    "jaipur": "Jaipur",
    "chandigarh": "Chandigarh",
    "mohali": "Mohali",
    "coimbatore": "Coimbatore",
    "kochi": "Kochi"
}


METRO_CITIES = [
    "bengaluru", "mumbai", "new delhi",
    "chennai", "hyderabad", "kolkata"
]

conn = get_db_connection()
cursor = conn.cursor()

for city_slug, city_name in cities.items():

    for page in range(1, 501):

        url = f"https://www.ambitionbox.com/list-of-companies?locations={city_slug}&page={page}"
        response = requests.get(url, headers=headers)

        if response.status_code == 404:
            print(f"Page not found: {city_name} page {page}")
            continue

        if response.status_code != 200:
            print(f"⚠️ Skipping page {page}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        cards = soup.find_all("div", class_="companyCardWrapper")

        print(f"{city_name} Page {page} → Cards: {len(cards)}")

        if len(cards) == 0:
            print(f"{city_name} finished at page {page}")
            break

        for card in cards:

            company = card.find("h2")
            rating = card.find("div", class_="rating_text")
            industry = card.find("span", class_="companyCardWrapper__interLinking")

            company_name = company.text.strip() if company else "Unknown"
            rating = float(rating.text.strip()) if rating else None

            industry = industry.text.split("|")[0].strip() if industry else None

            is_metro = "Yes" if city_slug.replace("-", " ") in METRO_CITIES else "No"

            cursor.execute("""
                INSERT INTO companies
                (company_name, rating, industry, city, metro_city, page)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (company_name, rating, industry, city_name, is_metro, page))

        conn.commit()
        time.sleep(0.5)

cursor.close()
conn.close()
print("Scraping completed")
