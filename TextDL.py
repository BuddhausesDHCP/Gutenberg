"""
Download a UTF-8 encoded text file from Project Gutenberg and save it to a specified path.

Requires:
- Python 3.6+
- requests library (`pip install requests`)
"""


import requests
from pathlib import Path

# URL of Text File (UTF-8 version)
url = "https://www.gutenberg.org/cache/epub/2701/pg2701.txt" # Example: Moby Dick

# Path to your Directory (including desired file name)
# Replace with actual value
    path = Path("/Users/yourname/Desktop/Moby_Dick.txt") #Example Moby_Dick.txt

# Download and save
response = requests.get(url)
path.write_text(response.text, encoding='utf-8')

print("Download complete. File saved to your Desktop.")
