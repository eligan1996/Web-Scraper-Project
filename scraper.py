import requests
import csv # 1. Import the CSV module
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# This will hold all our job data rows
job_data = [] 

job_cards = soup.find_all("div", class_="card-content")

for card in job_cards:
    # 1. Safely find the elements
    title_el = card.find("h2", class_="title")
    company_el = card.find("p", class_="subtitle")
    location_el = card.find("p", class_="location")
    
    # 2. Extract text with fallback
    title = title_el.text.strip() if title_el else "N/A"
    company = company_el.text.strip() if company_el else "N/A"
    location = location_el.text.strip() if location_el else "N/A"
    
    # 3. Explicitly define 'link' EVERY time
    links = card.find_all("a")
    if len(links) >= 2:
        link = links[1]["href"]
    else:
        link = "No link available"
        
    # 4. Now 'link' is guaranteed to exist, so this will work:
    job_data.append([title, company, location, link])

# 3. Write the data to a CSV file
with open('job_listings.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(["Title", "Company", "Location", "Link"])
    # Write all the job rows
    writer.writerows(job_data)

print("Scraping complete! Data saved to job_listings.csv")