import wikipedia
"""
Before using Sparql and konwledge graphs I wanted to build API wrappers for different sites and connect them via a NN, isn't used
"""

class wiki():
    def __init__(self):
        wikipedia.set_lang("en")

    def querry_for(self,topic):
        """
        Uses the suggestion method to check if input is valid and passes that to the search method.

        Inputs:
            topic: The topic to look for -> str
        Outputs:
            wikipedia.search(topic) -> str
        """
        suggestion=wikipedia.suggest(topic)
        if not suggestion:
            return wikipedia.search(topic, results=1)[0]
        else:
            return wikipedia.search(suggestion,results=1)[0]

    def get_data(self,search_result):
        """
        Uses the wikipedia.page(search_result).content method to return the content of the Wikipedia page.
        Inputs:
            search_result:
                The result of the querry_for method -> str
        Outputs:
            wikipedia.page.content -> str
        """
        return wikipedia.page(search_result).content

    def get_summary(self,search_result):
        """
        Uses the wikipedia.summary method for a summary.

        Inputs:
            search_result:
                The result of the querry_for method -> str
        Outputs:
            wikipedia.summary -> str
        """
        return wikipedia.summary(search_result,senteces=10)
