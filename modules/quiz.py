import bs4 as bs
from random import choice
from statics.quiz_topics import topics

def get_link(topic):
    for key in topics.keys():
        if key == topic:
            rval1 = choice(list(topics[key].keys()))
            subject = choice(topics[key][rval1]['topics'])
            return topics[key][rval1]['link'].format(subject)
        for subkey in topics[key].keys():
            if subkey == topic:
                subject = choice(topics[key][subkey]['topics'])
                return topics[key][subkey]['link'].format(subject)
            for subtopic in topics[key][subkey]['topics']:
                if subtopic == topic:
                    return topics[key][subkey]['link'].format(subtopic)
    return None

