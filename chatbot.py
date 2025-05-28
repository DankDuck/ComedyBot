from nltk.stem import PorterStemmer
from jokes import raw_jokes, joke_vectors
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
       topic_word_vector = nlp(topic_word).vector
       similar_dist = 100
       curr_index = 0
       similar_index = curr_index
       for joke in joke_vectors:
            for token_vector in joke:
                current_dist = cosine(token_vector, topic_word_vector)
                if current_dist < similar_dist:
                    similar_dist = current_dist
                    similar_index = curr_index
            curr_index += 1
       return similar_index

bot = ComedyBot()
bot.greet()
