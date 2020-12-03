"""
Before nlp backend this was the go to class to restructure a sentence, doesn't work aswell
"""


class QuestionParser():
    def __init__(self) -> None:
        self.mapEng = {
            "ADJ": "adjective",
            "ADP": "adposition",
            "ADV": "adverb",
            "AUX": "auxiliary verb",
            "CONJ": "coordinating conjunction",
            "DET": "determiner",
            "INTJ": "interjection",
            "NOUN": "noun",
            "NUM": "numeral",
            "PART": "particle",
            "PRON": "pronoun",
            "PROPN": "proper noun",
            "PUNCT": "punctuation",
            "SCONJ": "suordinating conjunction",
            "SYM": "symbol",
            "VERB": "verb",
            "X": "other"
        },
        self.engQuestionLayout: list = ["AUX", "PROPN", "VERB",]

    def englishParser(self, data: dict) -> list:
        storage: list = []
        sentences:dict = {}
        _string = ""
        count=1
        length = len(data.keys())+1
        for pos in range(1,length):
            for k,v in data[pos].items():
                _string+=" "+k
            print(_string)