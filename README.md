# Website Scraper Tool

A Python tool for automatically discovering and downloading files from websites. Scrapes web pages for downloadable files (PDFs, DOCX, XLSX, ZIP, CSV, etc.) and saves them locally.

## Features

- Automatically finds and downloads files from target URLs
- Supports multiple file types (PDF, DOCX, XLSX, ZIP, CSV)
- Handles duplicate filenames with automatic renaming
- Rate limiting to avoid overwhelming servers
- Error handling for network issues

## Requirements

- Python 3.6+
- requests
- beautifulsoup4

## Installation

1. Clone or download this repository
2. Install dependencies:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Edit `main.py` and configure:
   - `BASE_URL`: The website URL to scrape
   - `DOWNLOAD_DIR`: Directory where files will be saved (default: `downloaded_files`)
   - `FILE_TYPES`: List of file extensions to download

2. Run the scraper:

```bash
python main.py
```

## Configuration Example

```python
BASE_URL = "https://example.com/resources"
DOWNLOAD_DIR = "downloaded_files"
FILE_TYPES = ['pdf', 'docx', 'xlsx', 'zip', 'csv']
```

## How It Works

1. Fetches the target webpage
2. Parses all anchor tags for downloadable file links
3. Filters links by specified file extensions
4. Downloads each file to the specified directory
5. Automatically renames duplicates (e.g., `file_1.pdf`, `file_2.pdf`)

## Notes

- SSL verification is disabled (`verify=False`) - use with caution
- 1-second delay between downloads to be respectful to servers
- Ensure you have permission to scrape the target website
