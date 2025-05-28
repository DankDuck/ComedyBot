from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from bs4 import BeautifulSoup

import requests
import re
import spacy

nlp = spacy.load('en_core_web_md')
url1 = 'https://www.countryliving.com/life/a27452412/best-dad-jokes/'
response = requests.get(url1).text
soup = BeautifulSoup(response, 'html.parser')

joke_elements1 = soup.find_all('li')

url2 = 'https://www.menshealth.com/trending-news/a34437277/best-dad-jokes/'
response = requests.get(url2).text
soup = BeautifulSoup(response, 'html.parser')
joke_elements2 = soup.find_all('li')
joke_elements = joke_elements1.extend(joke_elements2)

raw_jokes = []
jokes = []
joke_vectors = []
stemmer = PorterStemmer()

for joke_elem in joke_elements2:
    joke_text = joke_elem.get_text(strip=True)
    if len(joke_text) >= 25:
        raw_jokes.append(joke_text)
        tokens = word_tokenize(re.sub(r'[\.\,\?\"]', '', joke_text))
        token_vectors = []
        for token in tokens:
            token = stemmer.stem(token).lower()
            token_vectors.append(nlp(token).vector)
        jokes.append(tokens)
        joke_vectors.append(token_vectors)
