from statics.quiz_topics import topics
from modules.quiz import get_topic_link, get_quiz, str_diff

# quiz = get_quiz(get_topic_link("biology"))
# print(quiz)
#print(get_questions(quiz))

# for key in topics.keys():
#     for subkey in topics[key].keys():
#         link = topics[key][subkey]["link"]
#         for topic in topics[key][subkey]["topics"]:
#             print(link.format(topic))

print(str_diff("sciunce", "science"))
print(str_diff("sciunce", "english"))