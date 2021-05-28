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

def get_questions(quiz_link):
    bs = get_page_soup(quiz_link)
    questions_text = [span.get_text() for span in bs.find_all("span", {"class": "TermText"})]
    if len(questions_text)%2 == 0:
        del questions_text[-1]
    qa = [[], []]
    for i in range(len(questions_text)):
        qa[i%2].append(questions_text[i])
    return list(zip(qa[0], qa[1]))
