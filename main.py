import csv
import requests
from bs4 import BeautifulSoup


def get_product_details(product_url):
    r = requests.get(product_url)
    soup = BeautifulSoup(r.text, "html.parser")

    try:
        description = soup.find(
            "div", class_="a-section a-spacing-small a-spacing-top-small"
        ).text.strip()
    except AttributeError:
        description = "Not available"

    try:
        asin = soup.find("th", string="ASIN").find_next("td").text.strip()
    except AttributeError:
        asin = "Not available"

    try:
        product_description = soup.find("div", id="productDescription").text.strip()
    except AttributeError:
        product_description = "Not available"

    try:
        manufacturer = (
            soup.find("th", string="Manufacturer").find_next("td").text.strip()
        )
    except AttributeError:
        manufacturer = "Not available"

    return {
        "Description": description,
        "ASIN": asin,
        "Product Description": product_description,
        "Manufacturer": manufacturer,
    }


def get_product_data(url):
    products = []

    for page_num in range(1, 5):
        url_with_page = f"{url}&page={page_num}"
        r = requests.get(url_with_page)
        soup = BeautifulSoup(r.text, "html.parser")

        for product in soup.find_all("div", class_="s-result-item"):
            try:
                product_url = (
                    "https://www.amazon.in"
                    + product.find("a", class_="a-link-normal s-no-outline")["href"]
                )
                product_info = get_product_details(product_url)

                product_data = {
                    "Product URL": product_url,
                    "Product Name": product.find(
                        "span", class_="a-size-medium a-color-base a-text-normal"
                    ).text,
                    "Product Price": product.find("span", class_="a-price-whole").text,
                    "Ratings": product.find("span", class_="a-icon-alt").text,
                    "Number Of Reviews": product.find(
                        "span", class_="a-size-base"
                    ).text.split()[0],
                    **product_info,
                }

                products.append(product_data)
            except Exception as e:
                print(f"Error: {e}")

    return products


url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%252"
product_data = get_product_data(url)

if product_data:
    csv_columns = product_data[0].keys()
    csv_file = "product_data.csv"

    with open(csv_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in product_data:
            writer.writerow(data)

    print(f"Data exported to {csv_file}")
else:
    print("No products found.")
