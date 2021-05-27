from random import choice
from statics.quiz_topics import topics
from utils.webscrapingutils import get_page_soup

flashcard_link_id = "https://quizlet.com/gb/"

def clean_topic(topic):
    return topic.strip().replace(" ", "-")

def get_topic_link(topic):
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

def get_quiz(topic_link):
    bs = get_page_soup(topic_link)
    links = [link["href"] for link in bs.find_all("a", href=True) if flashcard_link_id in link["href"]]
    return choice(links)

def get_question(quiz_link):
    bs = get_page_soup(quiz_link)
