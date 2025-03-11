import requests
import re
import csv
from bs4 import BeautifulSoup

# STEP 1: Add your SerpAPI and Hunter.io API Keys
SERPAPI_KEY = "YOUR_SERPAPI_CODE"
HUNTER_API_KEY = "YOUR_HUNTERIO_CODE"

# STEP 2: Modify search query for Milwaukee Manufacturing CEOs
QUERY = 'Milwaukee "manufacturing CEO" "@gmail.com" OR "@yahoo.com" OR "@outlook.com" OR "@company.com"'

# Hunter.io API for email verification
def verify_email(email):
    url = f"https://api.hunter.io/v2/email-verifier"
    params = {
        "email": email,
        "api_key": HUNTER_API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    if data.get('data', {}).get('status') == "valid":
        full_name = data.get('data', {}).get('first_name', '') + " " + data.get('data', {}).get('last_name', '')
        company = data.get('data', {}).get('organization', '')
        return {"email": email, "full_name": full_name, "company": company}
    return None

# Function to get Google search results via SerpAPI (LIMIT TO 50 RESULTS)
def get_google_results(query):
    url = "https://serpapi.com/search"
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_KEY,
        "num": 50  # Limit results to 50
    }
    response = requests.get(url, params=params)
    return response.json().get("organic_results", [])

# Function to extract emails from a webpage
def extract_emails_from_url(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
        return set(emails)  # Remove duplicates
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return set()

# Main function to find, verify, and extract emails
def scrape_emails():
    results = get_google_results(QUERY)
    all_verified_emails = []

    for result in results:
        url = result.get("link")
        print(f"Scraping: {url}")
        emails = extract_emails_from_url(url)
        
        for email in emails:
            verified_data = verify_email(email)
            if verified_data:
                all_verified_emails.append(verified_data)
            
            # Stop once we have 50 verified emails
            if len(all_verified_emails) >= 50:
                break
        if len(all_verified_emails) >= 50:
            break

    # Save verified data to CSV
    with open("milwaukee_verified_ceo_emails.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Email", "Full Name", "Company"])
        for entry in all_verified_emails:
            writer.writerow([entry["email"], entry["full_name"], entry["company"]])

    print(f"✅ Scraped {len(all_verified_emails)} verified emails and saved to milwaukee_verified_ceo_emails.csv")

# Run the script
scrape_emails()
