import os
import re
from statics.quiz_topics import topics
from modules.math_general import graph
from modules.facereplace import Memes
from modules.quiz import get_topic_link, get_quiz

# quiz = get_quiz(get_topic_link("biology"))
# print(quiz)
#print(get_questions(quiz))

# for key in topics.keys():
#     for subkey in topics[key].keys():
#         link = topics[key][subkey]["link"]
#         for topic in topics[key][subkey]["topics"]:
#             print(link.format(topic))

# expression = "y= 2x^2 + 34x - 34"
# nums = max(map(float, re.findall("[+-]?\d+(?:\.\d+)?", expression)))
print(Memes.PEPE.value)