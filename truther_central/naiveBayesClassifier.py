from nltk.classify import NaiveBayesClassifier as NltkNaiveBayesClassifier  # import nltk NaiveBayesClassifier package
from nltk.corpus import subjectivity  # import nltk subjectivity package
from nltk.sentiment import SentimentAnalyzer  # import nltk SentimentAnalyzer package
from nltk.sentiment.util import *  # import nltk Sentiment Utilities package
from nltk.tokenize import word_tokenize
import nltk
import logging as log

log.basicConfig(level=log.DEBUG)

class NaiveBayesClassifier:

    """
        naiveBayesClassifier.py
        Contains properties and logic for training and returning evaluation results of NaiveBayesClassifier
        Subjectivity corpora accreditation to Bo Pang and Lillian Lee, "A Sentimental Education: Sentiment Analysis
        Using Subjectivity Summarization Based on Minimum Cuts", Proceedings of the ACL, 2004
    """
    #  constructor the for NaiveBayesClassifier - we should move the constructor logic into a method later on
    def __init__(self):
        # the weighted score of objectivity and subjectivity scores
        self.weighted_score = 0
        # number of training documents
        self.n_instances = 100
        # list of nltk subjectivity training documents
        self.subj_docs = [(sent, 'subj') for sent in subjectivity.sents(categories='subj')[:self.n_instances]]
        # list of nltk objectivity training documents
        self.obj_docs = [(sent, 'obj') for sent in subjectivity.sents(categories='obj')[:self.n_instances]]
        # get the first 80 documents used for training subjectivity classifier
        self.train_subj_docs = self.subj_docs[:80]
        # get the remaining 20 documents for testing the subjectivity classifier
        self.test_subj_docs = self.subj_docs[80:100]
        # get the first 80 documents used for training objectivity classifier
        self.train_obj_docs = self.obj_docs[:80]
        # get the remaining 20 documents for testing the objectivity classifier
        self.test_obj_docs = self.obj_docs[80:100]
        # set training documents
        self.training_docs = self.train_subj_docs + self.train_obj_docs
        # self.training_docs = self.train_obj_docs
        # set testing documents
        self.testing_docs = self.test_subj_docs + self.test_obj_docs
        # create instance of nltk Sentiment Analyzer
        self.sentim_analyzer = SentimentAnalyzer()
        # get all the negative words from training documents
        self.all_words_neg = self.sentim_analyzer.all_words([mark_negation(doc) for doc in self.training_docs])
        # get all unigram features from negative words
        self.unigram_feats = self.sentim_analyzer.unigram_word_feats(self.all_words_neg, min_freq=4)
        # using the unigram features, create and attach a feature extractor to the sentiment analyser
        self.sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=self.unigram_feats)
        # set the training set using the sentiment analyzer
        self.training_set = self.sentim_analyzer.apply_features(self.training_docs)
        # run a test using the testing documents
        self.test_set = self.sentim_analyzer.apply_features(self.testing_docs)
        self.model = {}
        self.trainer = {}
        self.classifier = {}

    # method used to train the NaiveBayesClassifier
    def train_classifier(self):
        self.model = NltkNaiveBayesClassifier.train(self.training_set)
        self.trainer = NltkNaiveBayesClassifier.train
        self.classifier = self.sentim_analyzer.train(self.trainer, self.training_set)

    def classify_setence(self, sentence):
        if sentence is not None:
            if len(sentence) is not 0:
                return self.model.classify(self.format_sentence(sentence))
            else:
                return None
        else:
            return None

    def format_sentence(self, sentence):
        return {word: True for word in word_tokenize(sentence)}

    # return the results of the naive bayes classifier training phase
    def get_evaluation_results(self) -> object:
        # returns a sorted dictionary / hash map in alphabetical order

        return sorted(self.sentim_analyzer.evaluate(self.test_set).items())

    # return the results of the naive bayes classifier training phase
    # def get_polarity_scores(self, document_text):
    #     log.info(self.classifier.polarity_scores(document_text))
