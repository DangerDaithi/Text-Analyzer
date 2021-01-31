from truther_central import FileService as fileService
from truther_central import nltkService as nltkService
from truther_central import document as document
import logging as log

log.basicConfig(level=log.DEBUG)


def main():
    """
        main.py
        Main entry point to truther engine - will be replaced with api at later stage
    """
    # instance of Document
    doc = document.Document()
    # the file location of test news article
    file_path = '..\\resources\\test_article.txt'

    try:

        # read text of document
        text = fileService.FileService.read_file(file_path=file_path)

        # set the text of the document
        if text is not None:
            doc.set_doc_text(text)
            doc.set_top_term_count(10)
        else:
            raise ValueError('Text from document was null')

        # tokenize document text and tag part of speech
        if doc.get_doc_text() is not None:
            # tokenize the doc text
            doc.set_text_tokenized(nltkService.NltkService.tokenize(doc.get_doc_text()))
            # set the sentence tokenized array using document text
            doc.set_text_sentence_tokenized(nltkService.NltkService.tokenize_sentence(doc.get_doc_text()))
            # remove all punctuation
            doc.set_process_text_tokenized(nltkService.NltkService.remove_punctuation_tokenize(doc.get_doc_text()))
            # remove stop words (using doc tokenized with no punctuation)
            doc.set_text_tokenized_no_stop_words(nltkService.NltkService.remove_stop_words(doc.get_processed_text_tokenized()))
            # find parts of speech of document
            doc.set_text_pos_tagged(nltkService.NltkService.tag_part_of_speech(doc.get_processed_text_tokenized()))
            # find the n number of top terms in the document
            doc.set_top_terms(nltkService.NltkService.most_common(doc.get_processed_text_tokenized(), doc.get_top_term_count()))

            # log results of data-pre processing
            log.info(doc.get_text_tokenized())
            log.info(doc.get_processed_text_tokenized())
            log.info(doc.get_top_terms)
            log.info(doc.get_text_pos_tagged())
        else:
            raise ValueError('Text from document was null')

        # using the PorterStemmer, stem the tokenized text
        if doc.get_text_tokenized() is not None:
            doc.set_text_tokenized_stemmed(nltkService.NltkService.porter_stem(doc.get_text_tokenized()))
            log.info(doc.get_text_tokenized_stemmed())
        else:
            raise ValueError('Document unprocessed tokenized array is empty')

        # train the naive bayes classifier
        doc.perspective.naiveBayesClassifier.train_classifier()

        # log the evaluation results of the NaiveBayes training phase
        # for key, value in doc.perspective.naiveBayesClassifier.get_evaluation_results():
        #     log.info('{0}: {1}'.format(key, value))

        #for key, value in doc.perspective.naiveBayesClassifier.test(doc.get_text_sentence_tokenized()):
         #   log.info('{0}: {1}'.format(key, value))

        for sentence in doc.get_text_sentence_tokenized():
            result = doc.perspective.naiveBayesClassifier.classify_setence(sentence)
            log.info(result)

        # log the results of training the naive bayes classifer
        log.info(doc.perspective.subjectivity.get_score())

    except Exception as e:
        #  Log the error to the console
        log.error(e)


if __name__ == '__main__':
    main()
