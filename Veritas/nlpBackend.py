import spacy

class BasicFunctions():
    def __init__(self, language: str = "en") -> None:
        self.language: str = language# for later so you can add different languages
        self.model: str = f"{self.language}_core_web_sm"# find the language model
        self.s = spacy.load(self.model)# load the language model
        #self._tr = pytextrank.TextRank()#Useless
        #self.s.add_pipe(self._tr.PipelineComponent, name="textrank", last=True) aswell
        self.auxiliaryVerbs = ["have","be","was","were","am", "are", "is","may","might" ,"must","shall","should","will","would",]# should allow for custom sentences for each AUX verb, and to figure out if the sentence contains one
    
    """
    Useless
    def extractQuestions(self, data: str) -> list:
        '''Extracts questions'''
        store: list = []

        doc = self.s(data)  # converts text into a for spacy readable format
        displacy.serve(doc, style="dep")
        # for token in doc:
        #   store.append((token.text,token.pos_))
        # return store
"""
    def extractSentences(self, data: str) -> list:
        """Converts text sentences"""
        doc = self.s(data)
        return list(doc.sents)

    def tokenParser(self, sentences: list) -> dict:
        """Tokenizes sentences and store the words with there pos (part of speach) tag in the a dict with the number of the sentence (for later reconstruction)"""
        storage: dict = {}
        numSentences = len(sentences)
        currentSentence = 1
        for sentence in sentences:
            tempStorage: dict = {}
            print(sentence.text)
            doc = self.s(sentence.text)
            for token in doc:
                # print(token) DEBUG only
                tempStorage[token.text] = token.pos_
            storage[currentSentence] = tempStorage
            currentSentence += 1
        return storage
    
    def convertToQuestion(self,data:dict)->list:# very, very very limited real world usecases
        """Highlevel function which creates question sentences"""
        for keys, values in data.items():
            done:bool=False#checks if the first part is done
            key=None
            current:dict = values
            sentence:str = ""
            check = self._check(current)# can be either of type bool or dict
            print(type(check),check)# debugging
            if type(check)==bool and check==True:# if it contains a AUX tag which is not have
                key:int = self._getKeyByValue(current,"AUX")[0]# get the first auxiliary verb
                current.pop(key)#remove it from the dictionary
                for i in current.items():# iterate through the dictionary with words
                    if not done and check==True:# checks if we haven't added the AUX infront of the text already
                        sentence+=f"{key} "# adds it 
                        done=True# prevent's it from triggering the statment again
                    sentence+=f"{i[0]} "# adds other words to the sentence
            else:
                sentence=check
            #sentence = textblob.TextBlob(sentence).correct()
            print(sentence)
    
    def _check(self,dic:dict):#doens't really work, only in rare cases
        """Will check if text contains AUX verbs and tries to restructure the sentence"""
        newSentence =""
        aux = "AUX" in dic.values()
        #other = False
        for i in dic.keys():
            if i.lower() in self.auxiliaryVerbs:
                if i.lower()=="have":
                    wordsFound = self._extractInOrder(dic,["PRON","PART","VERB","ADV"])
                    newSentence=f"Do {wordsFound['PRON']} have {wordsFound['PART']} {wordsFound['VERB']} {wordsFound['ADV']} "
                    return newSentence
                    #print(newSentence)
        return aux
    def _getKeyByValue(self, dic:dict,value)->list:
        """Get's Key of a Dictionary by value for all matching keys"""
        keys=[]
        for i in dic.items():
            if i[1]==value:
                keys.append(i[0])
        return keys
    
    def _extractInOrder(self,dic:dict,extract:list)->dict:
        """Will extract word parts in order and save them in a dict"""
        store:dict = {}
        for i in extract:
           store[i]=self._getKeyByValue(dic,i)
        return store
"""
Just a test, not usefull
    def pagerank(self,data:str):
        doc = self.s(data)
        # examine the top-ranked phrases in the document
        print("----------------------------")
        for p in doc._.phrases:
            print("{:.4f} {:5d}  {}".format(p.rank, p.count, p.text))
            print(p.chunks)
"""