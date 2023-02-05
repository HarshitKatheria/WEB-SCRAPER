import requests
from bs4 import BeautifulSoup

web_url = 'https://www.reddit.com/r/learnprogramming/'

# fetching the response from the web_url 
response = requests.get(web_url)

soup = BeautifulSoup(response.text,'html.parser')

# Extract all links from the website 
links = [link.get('href') for link in soup.find_all('a')]

# Extract all images from the website 
images = [img.get('src') for img in soup.find_all('img')]

# Store the links and images in a list 
content = []

for link in links:
    content.append(('link', link))

for image in images:
    content.append(('image', image))

# Remove duplicates from the list
content = list(set(content))

# Print the final list of links and images
for item in content:
    print(item[0], ":", item[1])
