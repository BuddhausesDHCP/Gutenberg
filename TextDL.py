# Requires the Requests library to be installed before execution


import requests
from pathlib import Path

# URL of Text File (UTF-8 version)
url = "https://www.gutenberg.org/cache/epub/****/****.txt" # Enter the URL of the .txt file

# Path to your Directory (including desired file name)
path = Path('/****/****/****/directory/****.txt') # Enter the absolute path of your desired directory

# Download and save
response = requests.get(url)
path.write_text(response.text, encoding='utf-8')

print("Download complete. File saved to your Desktop.")
