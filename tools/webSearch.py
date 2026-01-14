from dotenv import load_dotenv
import os
import requests
import urllib.parse


load_dotenv()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

def get_content_from_url(url: str) -> str:
    """
    Fetches the text content of a given URL.
    """
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def keyword_search(keyword: str, num_results: int = 10) -> list[str]:
    """
    Perform a web search for a keyword and return a list of URLs.
    """
    api_key = os.getenv("GOOGLE_SEARCH_API_KEY")
    cx = "f6866f32f20534fd0"
    
    if not api_key:
        print("Error: GOOGLE_SEARCH_API_KEY not found in .env file.")
        return []

    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={urllib.parse.quote_plus(keyword)}&num={num_results}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        result = response.json()
        return [item['link'] for item in result.get("items", [])]
    except requests.exceptions.RequestException as e:
        print(f"Error during keyword search: {e}")
        return []