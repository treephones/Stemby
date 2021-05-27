from statics.quiz_topics import topics
from modules.quiz import get_link

print(get_link("genetics"))

# for key in topics.keys():
#     for subkey in topics[key].keys():
#         link = topics[key][subkey]["link"]
#         for topic in topics[key][subkey]["topics"]:
#             print(link.format(topic))