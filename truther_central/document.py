from truther_central import perspective


class Document:
    """
        document.py
        The document class representing a single document of text
    """

    def __init__(self):

        # the author of the document
        self.author = ""
        # the document text
        self.text = ""
        # the tokenized array of document text
        self.text_tokenized = []
        # the tokenized array of document text
        self.text_tokenized_no_stop_words = []
        # the tokenized array of document text, with no punctuation
        self.processed_text_tokenized = []
        # the documents overall perspective
        self.perspective = perspective.Perspective()
        # the parts of speech of the document
        self.text_pos_tagged = []
        # the top term sof the document (pre-stemming)
        self.top_terms = []
        # the number of top terms to find in the document
        self.top_term_count = 0
        # the stemmed tokenized array of document text
        self.text_tokenized_stemmed = []
        # array containing all sentences in document
        self.text_sent_tokenized = []

    def set_top_term_count(self, count: int):
        """
        Sets number of top terms to find in the document
        :param count: the number of top terms to count
        """
        self.top_term_count = count

    def get_top_term_count(self) -> int:
        """
        Gets the the number of top terms to count for the document
        :return:
        """
        if self.top_term_count is not None or 0:
            return self.top_term_count
        else:
            return None

    def set_doc_text(self, text: str):
        """
        Sets the unprocessed text of the document
        :param text: raw text input
        """
        self.text = text

    def get_doc_text(self) -> str:
        """
        Gets the unprocessed text of the document
        :return:
        """
        if self.text is not None:
            if len(self.text) is not 0:
                return self.text
            else:
                return None
        else:
            return None

    def set_text_tokenized(self, text: []):
        """
        Sets the tokenized unprocessed text of the document
        :param text: raw input text as tokenized array
        """
        self.text_tokenized = text

    def get_text_tokenized(self) -> []:
        """
        Gets the tokenized unprocessed text of the document
        :return:
        """
        if len(self.text_tokenized) is 0:
            return None
        else:
            return self.text_tokenized

    def set_text_sentence_tokenized(self, text: []):
        """
        Sets the sentence tokenized unprocessed text of the document
        :param text: raw input text as tokenized array
        """
        self.text_sent_tokenized = text

    def get_text_sentence_tokenized(self) -> []:
        """
        Gets the sentence tokenized unprocessed text of the document
        :return:
        """
        if len(self.text_sent_tokenized) is 0:
            return None
        else:
            return self.text_sent_tokenized

    def set_process_text_tokenized(self, tokenized_text: []):
        """
        Sets the processed tokenized text of the document passing in the tokenzied unprocessed text array
        :param tokenized_text:
        """
        self.processed_text_tokenized = tokenized_text

    def get_processed_text_tokenized(self) -> []:
        """
        Gets the processed tokenized unprocessed text of the document
        :return:
        """
        if len(self.processed_text_tokenized) is 0:
            return None
        else:
            return self.processed_text_tokenized

    def set_text_tokenized_no_stop_words(self, no_stop_words: []):
        """
        Sets the tokenized_no_stop_words array
        :param no_stop_words:
        """
        self.text_tokenized_no_stop_words = no_stop_words

    def get_text_tokenized_no_stop_words(self) -> []:
        """
        Gets the tokenized_no_stop_words array
        :return:
        """
        if self.text_tokenized_no_stop_words is not None:
            if len(self.text_tokenized_no_stop_words) is not 0:
                return self.text_tokenized_no_stop_words
            else:
                return None
        else:
            return None

    def set_text_pos_tagged(self, text_pos_tagged):
        """
        Sets the part of speech tokenized array
        :param text_pos_tagged:
        """
        self.text_pos_tagged = text_pos_tagged

    def get_text_pos_tagged(self) -> []:
        """
         Gets the part of speech tokenized array
         :return:
         """
        if self.text_pos_tagged is not None:
            if len(self.text_pos_tagged) is not 0:
                return self.text_pos_tagged
            else:
                None
        else:
            None

    def set_text_tokenized_stemmed(self, text_tokenized_stemmed):
        """
        Sets the processed stemmed tokenized text array of the document
        :param text_tokenized_stemmed:
        """
        self.text_tokenized_stemmed = text_tokenized_stemmed

    def get_text_tokenized_stemmed(self) -> []:
        """
         Gets the text_tokenized_stemmed array of document text
         :return:
         """
        if self.text_tokenized_stemmed is not None:
            if len(self.text_tokenized_stemmed) is not 0:
                return self.text_tokenized_stemmed
            else:
                return None
        else:
            return None

    def set_top_terms(self, top_terms):
        """
        Sets the top_terms array of the document
        :param top_terms:
        """
        self.top_terms = top_terms

    def get_top_terms(self) -> []:
        """
         Gets the top_terms array of the doc
         :return:
         """

        if self.top_terms is not None:
            if len(self.top_terms) is not 0:
                return self.top_terms
            else:
                return None
        else:
            return None
