from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from jokes import jokes, raw_jokes
from scipy.spatial.distance import cosine
import spacy
import time
nlp = spacy.load('en_core_web_md')

class ComedyBot():
   exit_commands = {"bye", "no", "exit", "cya", "nah"}

   stemmer = PorterStemmer()
   def preprocess(self, topic_word):
       input = self.stemmer.stem(topic_word)
       return input.lower()

   def greet(self):
       response = input("What topic would you like your joke on? ")
       self.give_funny(response)

   def make_exit(self, topic_word):
       for exit_command in self.exit_commands:
           if exit_command in topic_word:
               print("Bye!")
               return True
       return False

   def give_funny(self, topic_word):
       while not self.make_exit(topic_word):
           most_similar_index = self.find_most_similar_index(topic_word)
           if most_similar_index:
            print(raw_jokes[most_similar_index])
            time.sleep(1)
            topic_word = input("What's another topic you would a joke on? ")
           else:
               time.sleep(1)
               topic_word = input("What's another topic you would a joke on? ")

   def find_most_similar_index(self, topic_word):
       similarities = []
       for joke in jokes:
           similar_words = 0
           for token in joke:
               if topic_word == token:
                   similar_words += 1
           similarities.append(similar_words)
       max_similarities = max(similarities)
       if max_similarities:
           most_similar_index = similarities.index(max_similarities)
           return most_similar_index
       print("Please enter another (more basic) topic")

bot = ComedyBot()
bot.greet()

# Wanted to do this but too freaking buggy
# topic_word_vector = nlp(topic_word).vector
#         similar_dist = 100
#         most_similar_joke = "Blah blah"
#         for joke in joke_vectors:
#             for token_vector in joke:
#                 current_dist = cosine(token_vector, topic_word_vector)
#                 if current_dist < similar_dist and current_dist != 0:
#                     print("Found smaller distance")
#                     similar_dist = current_dist
#                     print(current_dist)
#                     print(joke_vectors.index(joke))
#                     # most_similar_joke = jokes[joke_vectors.index(joke)]
#         return most_similar_joke