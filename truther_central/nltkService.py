from nltk.tokenize import word_tokenize, sent_tokenize  # the nltk word tokenize module
from nltk.stem import PorterStemmer  # the nltk PorterStemmer Modul
from nltk.corpus import movie_reviews, stopwords
import random
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import abc  # potential training documents from abc news corpora
import logging as log

log.basicConfig(level=log.DEBUG)

class NltkService:
    """
        nltkService.py
        Using the nltk module this class performs generic nltk tasks
    """

    @staticmethod
    def tokenize(text: str) -> []:
        """
            Provided a string of text, tokenize the text into an array
            :param text: string containing the text to be tokenized
            :return: the tokenized text in an array using nltk word tokenizer
        """
        if text is not None:
            if text:
                return word_tokenize(text)
            else:
                return None
        else:
            return None

    @staticmethod
    def tokenize_sentence(text: str) -> []:
        """
            Provided a string of text, tokenize the text into an array each element representing a sentence in the document
            :param text: string contining the text to be tokenized
            :return: the tokenized sentence text in an array using nltk word tokenizer
        """
        if text is not None:
            if text:
                return sent_tokenize(text)
            else:
                return None
        else:
            return None

    @staticmethod
    def most_common(tokenized_text: [], num_of_terms) -> []:
        """
            Provided a string of text, tokenize the text into an array
            :param tokenized_text: array containing the tokenized text
            :param num_of_terms: int, the number of top terms to find
            :return: an array of the most common terms of length [num_of_terms]
        """
        if tokenized_text is not None:
            if num_of_terms is not None or 0:
                tokenized_text = nltk.FreqDist(tokenized_text)
                return tokenized_text.most_common(num_of_terms)
        else:
            return None

    @staticmethod
    def to_lower_case(tokenized_text: []) -> []:
        """
            Provided a string of text, tokenize the text into an array
            :param tokenized_text: tokenized text of the document
            :return: copy of array, words all lowercase
        """
        if tokenized_text is not None:
            if len(tokenized_text) is not 0:
                tokens = [token.lower() for token in tokenized_text]
                if tokens is not None or len(tokens) is not 0:
                    return tokens
        else:
            return None

    @staticmethod
    def remove_stop_words(tokenized_text: []) -> []:
        """
            Provided a string of text, tokenize the text into an array
            :param tokenized_text: tokenized text of the document
            :return: filtered array of tokenized text with stop words removed
        """
        if tokenized_text is not None:
            if len(tokenized_text) is not 0:
                filtered_words = [word for word in tokenized_text if word not in stopwords.words('english')]
                if filtered_words is not None or len(tokenized_text) is not 0:
                    return filtered_words
        else:
            return None

    @staticmethod
    def remove_punctuation_tokenize(text: str) -> []:
        """
            Provided a string of text, tokenize the text into an array removing all punctuation
            :param text: string contining the text to be tokenized
            :return: the tokenized text with no punctuation in an array using nltk word tokenizer
        """
        if text is not None:
            if text:
                reg_exp_tokenizer = RegexpTokenizer(r'\w+')
                return reg_exp_tokenizer.tokenize(text)
            else:
                return None
        else:
            return None


    @staticmethod
    def porter_stem(tokenized_text: []) -> []:
        """
            Provided an array of document text, stem each word using the PorterStemmer algorithm
            :param tokenized_text: array containing the text to be Stemmed
            :return: the tokenized text
        """
        if tokenized_text is not None:
            if len(tokenized_text) is not 0:
                ps = PorterStemmer()

                # array containing no stop words
                preprocessed = [ps.stem(plural) for plural in tokenized_text]

                if len(preprocessed) is not 0:
                    return preprocessed
                else:
                    return None
            else:
                return None
        else:
            return None

    @staticmethod
    def tag_part_of_speech(tokenized_text: []) -> []:
        """
            Provided an array of tokenized text, find part of speech (poc)
            :param tokenized_text (array)
            :return: the tokenized tagged text
        """
        text_pos_tagged = list()
        if len(tokenized_text) is not 0:
            for i in tokenized_text:
                tagged = nltk.pos_tag(i)
                text_pos_tagged.append(tagged)
            if len(text_pos_tagged) is not 0:
                return text_pos_tagged
            else:
                return None
        else:
            return None

    @staticmethod
    def movie_review_text_classifier():
        documents = [(list(movie_reviews.words(fileid)), category)
                     for category in movie_reviews.categories()
                     for fileid in movie_reviews.fileids(category)]
        random.shuffle(documents)  # shuffling bag of words features
        # take every word in every review, compile, find most pop words used,
        # of thse most pop words, which one appears in pos and neg text, search for those words in doc's
        # if any of those texts has more positive words or negative words, thats how we classify it
        # log.info(documents[0])
        all_words = []
        for w in movie_reviews.words():
            all_words.append(w.lower())

        all_words = nltk.FreqDist(all_words)
        log.info(all_words.most_common(15))
