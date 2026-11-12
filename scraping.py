
import requests
import csv
import time

from bs4 import BeautifulSoup
from urllib.parse import urljoin


# 1. Website configuration
BASE_URL = "https://books.toscrape.com/"
CSV_FILE = "books.csv"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; BookScraper/1.0)"
}


# 2. Fetch webpage with retry handling
def fetch_page(url, retries=3):

    for attempt in range(retries):

        try:
            response = requests.get(
                url,
                headers=HEADERS,
                timeout=10
            )

            response.raise_for_status()

            print("Status:", response.status_code)
            print("Page size:", len(response.text), "characters")

            return response

        except requests.RequestException as error:

            print(f"Attempt {attempt + 1} failed: {error}")

            time.sleep(2)

    print("Could not retrieve webpage.")
    return None


# 3. Scrape books from all pages
def scrape_books():

    books_data = []
    current_url = BASE_URL
    page_number = 1

    while current_url:

        print(f"\nScraping page {page_number}...")

        response = fetch_page(current_url)

        if response is None:
            break

        soup = BeautifulSoup(response.text, "html.parser")

        # Find all book articles
        books = soup.find_all(
            "article",
            class_="product_pod"
        )

        print(f"Found {len(books)} books on this page.")

        # Extract book information
        for book in books:

            title = book.find("h3").find("a")["title"]

            price = book.find(
                "p",
                class_="price_color"
            ).text.strip()

            rating = book.find(
                "p",
                class_="star-rating"
            )["class"][1]

            books_data.append({
                "title": title,
                "price": price,
                "rating": rating
            })

        # Find the next page
        next_button = soup.find(
            "li",
            class_="next"
        )

        if next_button:
            next_link = next_button.find("a")["href"]

            current_url = urljoin(current_url, next_link)

            page_number += 1

            time.sleep(0.5)

        else:
            current_url = None

    return books_data


# 4. Save results to CSV
def save_to_csv(books_data):

    if not books_data:
        print("No books collected. CSV was not created.")
        return

    with open(
        CSV_FILE,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=["title", "price", "rating"]
        )

        writer.writeheader()
        writer.writerows(books_data)

    print(f"\nSuccessfully saved {len(books_data)} books to {CSV_FILE}")


# 5. Main program
if __name__ == "__main__":

    print("BOOK WEB SCRAPER STARTED")

    books = scrape_books()

    # Display first five books
    print("\nFIRST FIVE BOOKS:")

    for book in books[:5]:
        print(
            f"{book['title']}: "
            f"{book['price']} | "
            f"Rating: {book['rating']}"
        )

    # Save all collected books
    save_to_csv(books)

    print("\nSCRAPING COMPLETED.")
