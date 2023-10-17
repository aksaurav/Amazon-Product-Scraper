# Amazon-Product-Scraper

This Python script allows you to scrape product information from Amazon using the provided search URL. It utilizes the requests library to fetch web pages, and BeautifulSoup for parsing the HTML content. The collected data is then exported to a CSV file for further analysis.

## Getting Started

### Prerequisites
Before running the script, ensure you have the following libraries installed:

> `csv`
> `requests`
> `beautifulsoup4`

You can install these dependencies using the following command:

```pip install csv requests beautifulsoup4```

### How to Use
1. Open the Python script in your preferred editor.
2. Replace the url variable with your desired Amazon search URL.
```url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%252"```
3. Run the script. It will fetch product details from multiple pages and save them to a CSV file named product_data.csv.
```python amazon_scraper.py```



