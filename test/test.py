import os
import re
from statics.quiz_topics import topics
from modules.math_general import solve
from modules.quiz import get_topic_link, get_quiz

# quiz = get_quiz(get_topic_link("biology"))
# print(quiz)
#print(get_questions(quiz))

# for key in topics.keys():
#     for subkey in topics[key].keys():
#         link = topics[key][subkey]["link"]
#         for topic in topics[key][subkey]["topics"]:
#             print(link.format(topic))

print(os.path.abspath(os.getcwd())[:-5])