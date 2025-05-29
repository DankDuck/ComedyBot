from nltk.stem import PorterStemmer
from jokes import raw_jokes, joke_vectors
from scipy.spatial.distance import cosine
import spacy
import time
import numpy as np
np.seterr(divide='ignore', invalid='ignore')
nlp = spacy.load('en_core_web_md')

class ComedyBot():
   exit_commands = {"bye", "exit", "cya", "nah"}

   stemmer = PorterStemmer()
# preprocess text
   def preprocess(self, topic_word):
       input = self.stemmer.stem(topic_word)
       return input.lower()

# starting greeting
   def greet(self):
       response = input("What topic would you like your joke on? ")
       self.give_funny(response)

# exit if user triggers exit command
   def make_exit(self, topic_word):
       for exit_command in self.exit_commands:
           if exit_command in topic_word:
               print("See you later ヽ(´▽`)/")
               return True
       return False

# repeat asking jokes until user stops
   def give_funny(self, topic_word):
       while not self.make_exit(topic_word):
           most_similar_index = self.find_most_similar_index(topic_word)
           if most_similar_index:
            print(raw_jokes[most_similar_index])
            # 1s delay
            time.sleep(1)
            topic_word = input("What's another topic you would a joke on? ")
        # if no similar joke found
           else:
               time.sleep(1)
               print("Joke not found! (˚ ˃̣̣̥⌓˂̣̣̥ )")
               topic_word = input("What's another topic you would a joke on? ")

# use word2vec to find closest word to topic word
   def find_most_similar_index(self, topic_word):
       topic_word_vector = nlp(topic_word).vector
       most_similar_dist = 100
       curr_index = 0
       most_similar_index = 0
       for joke in joke_vectors:
            for token_vector in joke:
                current_dist = cosine(token_vector, topic_word_vector)
                if current_dist < most_similar_dist:
                    most_similar_dist = current_dist
                    most_similar_index = curr_index
            curr_index += 1
       return most_similar_index

# bot declaration and activation
bot = ComedyBot()
bot.greet()
