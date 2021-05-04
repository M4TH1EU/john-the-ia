import re

import wikipedia
from translate import Translator

import sentences


def getDescription(name):
    wikipedia.set_lang("fr")

    try:
        page = wikipedia.page(name, auto_suggest=True)
    except:
        try:
            try:
                page = wikipedia.page(name, auto_suggest=False)
            except:
                wikipedia.set_lang("en")
                page = wikipedia.page(name, auto_suggest=False)
        except:
            return sentences.getRandomSentenceFromId('wikipediaNotFound')

    summary = re.sub("[\(\[].*?[\)\]]", "", page.summary)
    summary = summary.replace("Inc.", "Inc")
    summary = summary.split(". ")[0]
    if "en.wiki" in page.url:
        translator = Translator(to_lang="fr", from_lang="en")
        summary = translator.translate(summary)

    return summary