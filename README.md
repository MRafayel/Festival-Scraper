# Festival Information Scraper

This Python script scrapes event information from the Skiddle API and extracts detailed contact information for each festival listed. The script saves the results into JSON and HTML files for further analysis or use.

## Table of Contents

- [Requirements](#requirements)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Output](#output)
- [Notes](#notes)


## Requirements

To run this script, you'll need the following libraries:

- `requests`
- `beautifulsoup4`
- `lxml`
- `datetime`

You can install the required libraries using `pip`:

```bash
pip install requests beautifulsoup4 lxml
```
## Usage

To use the script, simply run it in your Python environment:

```bash
python fest_scraper.py
```
## How It Works

   1. **API Request Loop:**
       - The script sends requests to the Skiddle API to retrieve event data within a 5-mile radius, over a 31-day period, divided into multiple pages (8 events per page).
       - The datetime.now() function is used to dynamically generate the date range.


   2. **Saving API Response:**
       - The API response for each page is saved as a JSON file in the data directory.


   3. **Processing Event Data:**
       - For each event, the script fetches the event details page, scrapes it for the location URL, and further extracts venue contact details.


   4. **Data Extraction:**
       - The script extracts the following information for each festival:
           - Festival Name
           - Festival Date
           - Venue Contact Information (e.g., address, phone number, email, etc.)
       - If contact information is available, it is stored in a dictionary format.


   5. **Saving Results:**
       - All extracted festival information is compiled into a list and saved as fest_list_result.json.

## Output

   - JSON Files: Each page's event data is saved as index_{i}.json in the data directory.
   - HTML Files: The HTML source code of each festival's page is saved as fest_index_{i}.html in the data directory.
   - Final JSON File: The extracted festival information is saved as fest_list_result.json.

## Notes

   - The script handles potential errors, such as missing location URLs or contact information, by using exception handling.
   - The Skiddle API is used with a public key for demonstration purposes. You might need to replace this with your own API key for extensive use.