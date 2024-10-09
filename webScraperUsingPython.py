pip install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup
import csv

# Function to extract website data
def extract_data(url):
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Example: Extracting all the article titles from a blog or news website
    # Assuming the titles are within <h2> tags with class 'article-title'
    articles = soup.find_all('h2', class_='article-title')
    
    # List to store the extracted data
    data = []

    for article in articles:
        title = article.get_text(strip=True)
        link = article.find('a')['href']  # Get the link (assuming it's an anchor tag inside <h2>)
        data.append({'title': title, 'link': link})

    return data

# Function to save extracted data to a CSV file
def save_to_csv(data, filename='scraped_data.csv'):
    # Define the column names
    fieldnames = ['title', 'link']

    # Open the CSV file for writing
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write the header row
        writer.writeheader()

        # Write the data rows
        for row in data:
            writer.writerow(row)

    print(f"Data saved to {filename}")

# Main function
if __name__ == '__main__':
    # URL of the website to scrape (replace with the desired website)
    url = 'https://example.com/blog'

    # Extract data from the website
    scraped_data = extract_data(url)

    # If data extraction was successful, save it to a CSV file
    if scraped_data:
        save_to_csv(scraped_data)
