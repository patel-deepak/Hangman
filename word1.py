
import random

my_file = open("word.txt").read()
word_list = my_file.split()
# print(word_list)
word=random.choice(word_list)
# print(word)

