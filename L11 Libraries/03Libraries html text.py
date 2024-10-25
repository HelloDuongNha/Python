import bs4  # Beautiful Soup - for parsing html content
import html_text  # for extracting visible text from html content
import requests  # for downloading a web page

response = requests.get("https://www.gre.ac.uk/")
soup = bs4.BeautifulSoup(response.text, "html.parser")
text = html_text.extract_text(str(soup))
print(text)
