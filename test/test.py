from statics.quiz_topics import topics
from modules.quiz import get_topic_link, get_quiz

print(get_quiz(get_topic_link("music")))

# for key in topics.keys():
#     for subkey in topics[key].keys():
#         link = topics[key][subkey]["link"]
#         for topic in topics[key][subkey]["topics"]:
#             print(link.format(topic))