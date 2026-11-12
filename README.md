# Book Web Scraper

A Python web scraping application that extracts book information from [Books to Scrape](https://books.toscrape.com/).

The application collects book titles, prices, and star ratings and saves the results into a CSV file.

## Features

- Scrapes book information from a website.
- Extracts book titles.
- Collects book prices.
- Retrieves star ratings.
- Automatically navigates through multiple pages.
- Handles connection errors using retry attempts.
- Uses request timeouts.
- Saves collected information into a CSV file.
- Displays the first five collected books.

## Technologies Used

- Python
- Requests
- BeautifulSoup
- CSV
- Time

## Project Structure

```text
book_web_scraper/
│
├── scraper.py
├── README.md
└── books.csv
```

## Installation

Install the required libraries:

```bash
pip install requests beautifulsoup4
```

## How to Run

Execute the following command:

```bash
python scraper.py
```

## Output

The scraper generates a file called `books.csv` containing:

| Title | Price | Rating |
|---|---|---|
| Book title | £51.77 | Three |
| Book title | £23.88 | Five |

*Prices and ratings above are illustrative.*

## Error Handling

The application includes:
- Three connection attempts.
- A 10-second request timeout.
- HTTP status validation.
- Automatic retry delays.

## Learning Objectives

This project demonstrates:
- Making HTTP requests.
- Extracting information from HTML.
- Working with BeautifulSoup.
- Navigating multiple webpages.
- Handling exceptions.
- Writing data into CSV files.

## Future Improvements

- Add book descriptions.
- Collect book availability.
- Store data in a database.
- Schedule automatic scraping.
- Export results to Excel.

## Author

Developed as part of my Python and AI automation learning journey.