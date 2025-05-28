from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from bs4 import BeautifulSoup

import requests
import re
import spacy

nlp = spacy.load('en_core_web_md')
# have to add this :(
# import nltk
# nltk.download('wordnet')
url = 'https://www.countryliving.com/life/a27452412/best-dad-jokes/'
response = requests.get(url)
html = response.text 
soup = BeautifulSoup(html, 'html.parser')

joke_elements = soup.find_all('li')

raw_jokes = []
jokes = []
joke_vectors = []
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
   
for joke_elem in joke_elements:
    joke_text = joke_elem.get_text(strip=True)
    if len(joke_text) >= 25:
        raw_jokes.append(joke_text)
        tokens = word_tokenize(re.sub(r'[\.\,\?\"]', '', joke_text))
        token_vectors = []
        for token in tokens:
            token = stemmer.stem(token).lower()
            token = lemmatizer.lemmatize(token)
            token_vectors.append(nlp(token).vector)
        jokes.append(tokens)
        joke_vectors.append(token_vectors)

