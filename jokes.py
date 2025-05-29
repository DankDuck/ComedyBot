from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from bs4 import BeautifulSoup

import numpy as np
import requests
import re
import spacy

nlp = spacy.load('en_core_web_md')

# get urls
def get_url_jokes(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    element_jokes = soup.find_all('li')
    return element_jokes

# get sites
joke_elements1 = get_url_jokes('https://www.countryliving.com/life/a27452412/best-dad-jokes/')
joke_elements2 = get_url_jokes('https://www.menshealth.com/trending-news/a34437277/best-dad-jokes/')
joke_elements3 = get_url_jokes('https://www.thepioneerwoman.com/home-lifestyle/a35617884/best-dad-jokes/')

joke_elements = joke_elements1 + joke_elements2 + joke_elements3

raw_jokes = []
joke_vectors = []
stemmer = PorterStemmer()

# add each indiv word to a list and its 'number values'
for joke_elem in joke_elements:
    joke_text = joke_elem.get_text(strip=True)
    if len(joke_text) >= 25:
        raw_jokes.append(joke_text)
        tokens = word_tokenize(re.sub(r'[\.\,\?\"]|.*Jokes.*', '', joke_text))
        token_vectors = []
        for token in tokens:
            token = stemmer.stem(token).lower()
            word_vector = nlp(token).vector
            if not np.all(word_vector == 0):
                token_vectors.append(str(word_vector))
        joke_vectors.append(token_vectors)
