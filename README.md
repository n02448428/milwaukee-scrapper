# milwaukee-scrapper
This script scrapes Google search results for publicly available email addresses of Milwaukee-based manufacturing CEOs. It then verifies the extracted emails using the Hunter.io API and saves valid entries to a CSV file.

## Features
- Uses SerpAPI to retrieve Google search results.
- Extracts email addresses from web pages.
- Verifies emails with Hunter.io API.
- Saves verified emails, names, and company information to a CSV file.

## Requirements
- Python 3.x
- `requests`, `beautifulsoup4`, and `csv` libraries
- SerpAPI and Hunter.io API keys

## Installation
1. Clone or download this repository.
2. Install dependencies:
   ```sh
   pip install requests beautifulsoup4
   ```

## Setup
1. Replace `SERPAPI_KEY` and `HUNTER_API_KEY` in `milwaukee_scraper.py` with your API keys.
2. Modify `QUERY` if you want to search for different industries or locations.

## Usage
Run the script with:
```sh
python milwaukee_scraper.py
```

## Output
The script generates a CSV file named `milwaukee_verified_ceo_emails.csv` with the following columns:
- Email
- Full Name
- Company

## Notes
- The script is limited to retrieving 50 results from SerpAPI.
- Ensure compliance with data privacy laws before using scraped email addresses.

## License
This project is available for personal and educational use. Please credit the original developer.

## Disclaimer
Scraping public data must comply with legal and ethical guidelines. Use responsibly.

