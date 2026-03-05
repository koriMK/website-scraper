import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse

# configuration
BASE_URL = "https://www.example.com"  # Change this to the target website
DOWNLOAD_DIR = "downloaded_files"
FILE_TYPES = ['pdf', 'docx', 'xlsx', 'zip', 'csv']  # Add more file types as needed (lowercase)


def get_download_links(url):
    """Fetch the page at *url*, parse for anchors and return
    absolute URLs that end with one of the extensions in FILE_TYPES."""

    try:
        # turn off verification if the environment lacks CA certs;
        # you can also install the `certifi` package or system "ca-certificates".
        r = requests.get(url, timeout=10, verify=False)
        r.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

    soup = BeautifulSoup(r.text, "html.parser")
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        full = urljoin(url, href)
        parsed = urlparse(full)
        if parsed.scheme not in ("http", "https"):
            continue
        if any(full.lower().endswith(ext) for ext in FILE_TYPES):
            links.append(full)
    return links

def download_file(url, download_dir):
    """Download *url* into *download_dir*, creating the directory if needed.
    This is the original logic that used to live in get_download_links."""
    if not os.path.exists(download_dir):
        os.makedirs(download_dir, exist_ok=True)

    base_filename = url.split("/")[-1] or "index"
    filepath = os.path.join(download_dir, base_filename)

    counter = 1
    while os.path.exists(filepath):
        name, ext = os.path.splitext(base_filename)
        filepath = os.path.join(download_dir, f"{name}_{counter}{ext}")
        counter += 1

    print(f"Downloading: {url} to {filepath}")
    try:
        with requests.get(url, stream=True, timeout=10, verify=False) as r:
            r.raise_for_status()
            with open(filepath, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        print(f"Saved: {filepath}")
    except requests.RequestException as e:
        print(f"Error downloading {url}: {e}")


def main():
    print(f"Fetching links from: {BASE_URL}")
    links = get_download_links(BASE_URL)
    if not links:
        print("No downloadable links found.")
        return

    print(f"Found {len(links)} files to download.")
    for url in links:
        download_file(url, DOWNLOAD_DIR)
        time.sleep(1)  # Sleep to avoid overwhelming the server

    print("Download completed.")

if __name__ == "__main__":
    import time
    main()
