from bs4 import BeautifulSoup
import requests
import pandas as pd

# ---------------------------scraping local file----------------------------
# with open("website.html", "r") as data:
#     file = data.read()
#
# soup = BeautifulSoup(file, "html.parser")
# print(soup.find_all(name="a"))

# --------------------------scraping live website---------------------------
# response = requests.get(url="https://news.ycombinator.com/")
# yc_webpage = response.text
#
# soup = BeautifulSoup(yc_webpage, "html.parser")
#
# article_tag = soup.find_all(name="a", class_="storylink")
#
# article_texts = []
# article_links = []
#
# for tag in article_tag:
#     article_text = tag.getText()
#     article_link = tag.get("href")
#     article_texts.append(article_text)
#     article_links.append(article_link)
#
# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
#
# print(article_texts)
# print(article_links)
# print(article_upvotes)
#
# largest_value = max(article_upvotes)
# largest_index = article_upvotes.index(largest_value)
# print(article_texts[largest_index])
# print(article_links[largest_index])

# --------------------------scraping pubmed---------------------------
response = requests.get(url="https://pubmed.ncbi.nlm.nih.gov/?term=%22burkitt%22+AND+%22mutation%22")
pubmed_search = response.text

soup = BeautifulSoup(pubmed_search, "html.parser")
titles = [title.getText().strip() for title in soup.find_all(name="a", class_="docsum-title")]
author_list = [names.getText() for names in soup.find_all(name="span", class_="docsum-authors full-authors")]
citations = [citation.getText() for citation in soup.find_all(name="span", class_="docsum-journal-citation full-journal-citation")]
links = [f"https://pubmed.ncbi.nlm.nih.gov{link.get('href')}" for link in soup.find_all(name="a", class_="docsum-title")]

references_data = pd.DataFrame(
    {'Title': titles,
     'Authors': author_list,
     'Citation': citations,
     'Link': links
     })

print(references_data)
