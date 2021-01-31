import unittest
from truther_central import document
from truther_central import nltkService as nltkService

import logging as log
log.basicConfig(level=log.DEBUG)


class TestNltkService(unittest.TestCase):

    """
        Unit testing for document functionality
    """

    @classmethod
    def setUpClass(cls):
        log.info("Set up class TestNltkService")

    @classmethod
    def tearDownClass(cls):
        log.info("Tear down class TestNltkService")

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

    def test_porter_stemmer(self):
        """
        Test nltk service class correctly returns an array of stemmed words
        """
        # some test text to be stemmed
        test_text = "This is a bunch of text that needs to be stemmed so lets" \
                    " stem it. I also really like pythoning like a pythoner using python!"

        # the expected result
        expected = ["Thi",
                    "is",
                    "a",
                    "bunch",
                    "of",
                    "text",
                    "that",
                    "need",
                    "to",
                    "be",
                    "stem",
                    "so",
                    "let",
                    "stem",
                    "it",
                    ".",
                    "I",
                    "also",
                    "realli",
                    "like",
                    "python",
                    "like",
                    "a",
                    "python",
                    "use",
                    "python",
                    "!"]

        doc = document.Document()

        # set the documennt text
        doc.set_doc_text(test_text)

        # set the tokenized doc text
        doc.set_text_tokenized(nltkService.NltkService.tokenize(doc.get_doc_text()))

        # set pocessed text using porter stemmer service
        doc.set_process_text_tokenized(nltkService.NltkService.porter_stem(doc.get_text_tokenized()))

        # the actual result
        actual = doc.get_processed_text_tokenized()

        # assert lengths are the same
        self.assertEqual(len(actual), len(expected))

        # assert that each word  in array is stemmed correctly
        for index in range(len(actual)):
            self.assertEqual(actual[index], expected[index])

        # test error handling
        actual = nltkService.NltkService.porter_stem(None)
        expected = None
        self.assertEqual(actual, expected)

        # test error handling
        actual = nltkService.NltkService.porter_stem("")
        expected = None
        self.assertEqual(actual, expected)

        log.info("Test Success: %s" % self.trim_id(unittest.TestCase.id(self)) + "\n")

    def test_to_lower_case(self):
        """
        Test nltk service to_lower_case correctly returns a lowercase string array
        """
        # some test text to be stemmed
        test_text = "LOOK AT all OF This Upper CAse madness SO NEEDS TO BE LowerCase"
        test_text_tokenized = nltkService.NltkService.tokenize(test_text)
        expected = ["look", "at", "all", "of", "this", "upper", "case", "madness",
                    "so", "needs", "to", "be", "lowercase"]# the expected result

        actual = nltkService.NltkService.to_lower_case(test_text_tokenized)

        # assert top terms are the same
        self.assertEqual([x[0] for x in actual], [x[0] for x in expected])
        self.assertEqual([x[1] for x in actual], [x[1] for x in expected])

        # test error handling
        actual = nltkService.NltkService.to_lower_case(None)
        expected = None
        self.assertEqual(actual, expected)

        log.info("Test Success: %s" % self.trim_id(unittest.TestCase.id(self)) + "\n")

    def test_most_common(self):
        """
        Test nltk service most_common correctly returns an array of top terms
        """
        # some test text to be stemmed
        test_text = "love love love fair joy python python python great hate hate another bunch of random text python"
        test_text_tokenized = nltkService.NltkService.tokenize(test_text)
        expected = [('python', 4), ('love', 3), ('hate', 2)]# the expected result

        actual = nltkService.NltkService.most_common(test_text_tokenized, 3)

        # assert top terms are the same
        self.assertEqual([x[0] for x in actual], [x[0] for x in expected])
        self.assertEqual([x[1] for x in actual], [x[1] for x in expected])

        # test error handling
        actual = nltkService.NltkService.most_common(None, 3)
        expected = None
        self.assertEqual(actual, expected)

        actual = nltkService.NltkService.most_common(test_text_tokenized, None)
        expected = None
        self.assertEqual(actual, expected)

        log.info("Test Success: %s" % self.trim_id(unittest.TestCase.id(self)) + "\n")

    def remove_punctuation_test(self):
        """
        Test nltk service remove_punctuation
        """
        # some test text to be stemmed
        test_text = "Man, look at all of this punctuation! @my_twitter #punctuation..."
        expected = ["Man", "look", "at", "all", "of", "this", "punctuation", "my_twitter", "punctuation"]

        actual = nltkService.NltkService.remove_punctuation_tokenize(test_text)

        # assert top terms are the same
        self.assertEqual(len(actual), len(expected))
        self.assertEqual(actual[0], expected[0])
        self.assertEqual(actual[1], expected[1])
        self.assertEqual(actual[2], expected[2])
        self.assertEqual(actual[3], expected[3])
        self.assertEqual(actual[4], expected[4])
        self.assertEqual(actual[5], expected[5])
        self.assertEqual(actual[6], expected[6])

        # test error handling
        actual = nltkService.NltkService.remove_punctuation_tokenize(None)
        expected = None
        self.assertEqual(actual, expected)

        actual = nltkService.NltkService.remove_punctuation_tokenize("")
        expected = None
        self.assertEqual(actual, expected)

        log.info("Test Success: %s" % self.trim_id(unittest.TestCase.id(self)) + "\n")

    def remove_atop_words_test(self):
        """
        Test nltk service remove_stop_words
        """
        # some test text to be stemmed
        tokenized = ["We", "have", "got", "to", "get", "rid", "of", "all", "of", "these", "stop", "words", "They",
                     "have", "no", "meaning"]
        expected = ['We', 'got', 'get', 'rid', 'stop', 'words', 'They', 'meaning']

        actual = nltkService.NltkService.remove_stop_words(tokenized)

        # assert top terms are the same
        self.assertEqual(len(actual), len(expected))
        self.assertEqual(actual[0], expected[0])
        self.assertEqual(actual[1], expected[1])
        self.assertEqual(actual[2], expected[2])
        self.assertEqual(actual[3], expected[3])
        self.assertEqual(actual[4], expected[4])
        self.assertEqual(actual[5], expected[5])
        self.assertEqual(actual[6], expected[6])

        # test handling of empty array
        actual = nltkService.NltkService.remove_stop_words(None)
        expected = None
        self.assertEqual(actual, expected)

        tokenized = []
        self.assertEqual(actual, expected)
        actual = nltkService.NltkService.remove_stop_words(tokenized)
        self.assertEqual(actual, expected)

        log.info("Test Success: %s" % self.trim_id(unittest.TestCase.id(self)) + "\n")