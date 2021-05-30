from random import choice
from statics.quiz_topics import topics
from utils.webscrapingutils import get_page_soup, str_diff

flashcard_link_id = "https://quizlet.com/gb/"

class TopicNotFoundException(Exception):
    def __init__(self, entered, suggested):
        self.entered = entered
        self.suggested = suggested

def clean_topic(topic):
    return topic.strip().replace(" ", "-").lower()

#locally
async def get_topic_link(topic):
    diffs = []
    for key in topics.keys():
        if key == topic:
            rval1 = choice(list(topics[key].keys()))
            subject = choice(topics[key][rval1]['topics'])
            return topics[key][rval1]['link'].format(subject)
        diffs.append((key, str_diff(topic, key)))
        for subkey in topics[key].keys():
            if subkey == topic:
                subject = choice(topics[key][subkey]['topics'])
                return topics[key][subkey]['link'].format(subject)
            diffs.append((subkey, str_diff(topic, subkey)))
            for subtopic in topics[key][subkey]['topics']:
                if subtopic == topic:
                    return topics[key][subkey]['link'].format(subtopic)
                diffs.append((subtopic, str_diff(topic, subtopic)))
    suggested = min(diffs, key=lambda pair: pair[1])[0]
    raise TopicNotFoundException(topic, suggested)

async def get_quiz(topic_link):
    bs = await get_page_soup(topic_link)
    links = [link["href"] for link in bs.find_all("a", href=True) if flashcard_link_id in link["href"]]
    return choice(links)

async def get_questions(quiz_link):
    bs = await get_page_soup(quiz_link)
    questions_text = [span.get_text() for span in bs.find_all("span", {"class": "TermText"})]
    if len(questions_text)%2 == 0:
        del questions_text[-1]
    qa = [[], []]
    for i in range(len(questions_text)):
        qa[i%2].append(questions_text[i])
    return list(zip(qa[0], qa[1]))
