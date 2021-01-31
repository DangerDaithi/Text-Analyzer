import unittest
from truther_central import document
from truther_central import nltkService as nltkService

import logging as log
log.basicConfig(level=log.DEBUG)


class TestDocument(unittest.TestCase):

    """
        Unit testing for document functionality
    """

    @classmethod
    def setUpClass(cls):
        log.info("Set up class TestDocument")

    @classmethod
    def tearDownClass(cls):
        log.info("Tear down class TestDocument")

    def setUp(self):
        log.info("Set up test and run %s" % self.trim_id(unittest.TestCase.id(self)))

    def tearDown(self):
        log.info("Tear down %s" % self.trim_id(unittest.TestCase.id(self)) + "\n")

    @staticmethod
    def trim_id(original: str, trim="unit_tests.test_document.") -> str:
        """
        Removes unnecessary detail from unit_test identifiers (unittest.TestCase.id)
        If substring to be removed is not present, supplied string is returned in full.

        :param original: string to be 'trimmed'
        :param trim: substring to remove from original
        :return: string minus removed substring
        """
        return original.replace(trim, "")

    def test_constructor_attributes_not_none(self):
        """
        Test that the constructor attributes in the Document class are not 'None'
        """
        doc = document.Document()

        self.assertIsNotNone(doc.author, msg="doc.author was empty")
        self.assertIsNotNone(doc.text, msg="doc.text was empty")
        self.assertIsNotNone(doc.text_tokenized, msg="doc.text_tokenized was empty")
        self.assertIsNotNone(doc.processed_text_tokenized, msg="doc.processed_text_tokenized was empty")
        self.assertIsNotNone(doc.perspective, msg="doc.perspective was empty")

        log.info("Test Success: %s" % self.trim_id(unittest.TestCase.id(self)) + "\n")

    def test_set_and_get_values_are_equal(self):
        """
        Test that the values return by document getters match the value given to the document getters
        """
        test_text = "This is some test document text"

        doc = document.Document()

        doc.set_doc_text(test_text)
        doc.set_process_text_tokenized(test_text)
        doc.set_text_tokenized(test_text)

        self.assertEqual(doc.get_doc_text(), test_text,
                         msg="Expected: %s, actual: %s" % (test_text, doc.get_doc_text()))
        self.assertEqual(doc.get_text_tokenized(), test_text,
                         msg="Expected: %s, actual: %s" % (test_text, doc.get_text_tokenized()))

        # test error handling
        doc.set_doc_text(None)
        actual = doc.get_doc_text()
        expected = None
        self.assertEqual(actual, expected)

        # test error handling
        doc.set_doc_text("")
        actual = doc.get_doc_text()
        expected = None
        self.assertEqual(actual, expected)

        log.info("Test Success: %s" % self.trim_id(unittest.TestCase.id(self)) + "\n")

    def test_set_and_get_top_term_count(self):
        """
        Tests the correct value for top terms in document can be set and retrieved correctly
        """

        doc = document.Document()

        doc.set_top_term_count(15)
        expected = 15

        self.assertEqual(doc.get_top_term_count(), expected,
                         msg="Expected: %s, actual: %s" % (expected, doc.get_top_term_count()))
        self.assertNotEqual(doc.get_top_term_count(), 12,
                         msg="Expected: %s, actual: %s" % (12, doc.get_top_term_count()))
        self.assertNotEqual(doc.get_top_term_count(), "34",
                         msg="Expected: %s, actual: %s" % ("34", doc.get_top_term_count()))

        # test error handling
        doc.set_top_term_count(None)
        expected = None
        actual = doc.get_top_term_count()
        self.assertEqual(actual,expected)
        log.info("Test Success: %s" % self.trim_id(unittest.TestCase.id(self)) + "\n")

    def test_set_and_get_top_term_array(self):
        """
        Tests the setting and getting of top terms array for document
        """
        top_terms = ["python", "is", "defo", "awesome"]

        doc = document.Document()

        doc.set_top_terms(top_terms)
        actual_top_terms = doc.get_top_terms()

        self.assertEqual(len(actual_top_terms), len(top_terms),
                         msg="Expected: %s, actual: %s" % (len(actual_top_terms), len(top_terms)))

        self.assertEqual(top_terms[1], actual_top_terms[1],
                         msg="Expected: %s, actual: %s" % (top_terms[1], actual_top_terms[1]))

        log.info("Test Success: %s" % self.trim_id(unittest.TestCase.id(self)) + "\n")

    def test_set_and_get_stemmed_array(self):
        """
        Tests the setting and getting of stemmed array for document
        """
        terms = ["python", "is", "defo", "awesome", "yo"]

        doc = document.Document()

        doc.set_text_tokenized_stemmed(terms)
        actual_terms = doc.get_text_tokenized_stemmed()

        self.assertEqual(len(actual_terms), len(terms),
                         msg="Expected: %s, actual: %s" % (len(actual_terms), len(terms)))

        self.assertEqual(terms[1], actual_terms[1],
                         msg="Expected: %s, actual: %s" % (terms[1], actual_terms[1]))

        log.info("Test Success: %s" % self.trim_id(unittest.TestCase.id(self)) + "\n")

    def test_set_and_get_processed_array(self):
        """
        Tests the setting and getting of no punctuation array for document
        """
        terms = ["python", "is", "defo", "awesome", "yo"]

        doc = document.Document()

        doc.set_process_text_tokenized(terms)
        actual_terms = doc.get_processed_text_tokenized()

        self.assertEqual(len(actual_terms), len(terms),
                         msg="Expected: %s, actual: %s" % (len(actual_terms), len(terms)))

        self.assertEqual(terms[1], actual_terms[1],
                         msg="Expected: %s, actual: %s" % (terms[1], actual_terms[1]))

        log.info("Test Success: %s" % self.trim_id(unittest.TestCase.id(self)) + "\n")

    def test_set_and_get_no_stop_words_array(self):
        """
        Tests the setting and getting of stop words removed array for document
        """
        terms = ["python", "is", "defo", "awesome", "yo", "no", "stop", "words"]

        doc = document.Document()

        doc.set_text_tokenized_no_stop_words(terms)
        actual_terms = doc.get_text_tokenized_no_stop_words()

        self.assertEqual(len(actual_terms), len(terms),
                         msg="Expected: %s, actual: %s" % (len(actual_terms), len(terms)))

        self.assertEqual(terms[6], actual_terms[6],
                         msg="Expected: %s, actual: %s" % (terms[1], actual_terms[1]))

        log.info("Test Success: %s" % self.trim_id(unittest.TestCase.id(self)) + "\n")