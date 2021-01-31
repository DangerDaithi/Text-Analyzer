#!flask/bin/python
import json
from truther_central import document
from truther_central import nltkService
from truther_central import FileService as fileService

from flask import Flask, send_file, request
# from flask_restful import Api

import logging as log
log.basicConfig(level=log.DEBUG)

app = Flask(__name__)
# api = Api(app)


@app.route("/")
def index():
    return send_file("static/index.html")


@app.route("/create", methods=['POST'])
def create():
    return "create received"

@app.route("/textResource", methods=['POST'])
def textResource():
    """
        Read file from given resource argument, and return text as JSON
        :param resource: string representing the location of the file to read from
        :return: resource text as JSON
    """
    resource = str(request.data, 'utf-8')
    # remove inverted commas from the resource text
    resource = resource[1:-1]
    # the file location of test news article
    file_path = '..\\resources\\' + resource + '.txt'
    resource_text = fileService.FileService.read_file(file_path=file_path)
    return json.dumps(resource_text)

@app.route("/analyze", methods=['POST'])
def post():
    # parse binary data (python 3) to json string
    text = str(request.data, 'utf-8')

    if text is not None:
        if len(text) is not 0:
            # instance of Document
            doc = document.Document()
            doc.set_doc_text(text)
            doc.set_top_term_count(20)
            # tokenize document text
            if doc.get_doc_text() is not None:
                # tokenize the doc text
                doc.set_text_tokenized(nltkService.NltkService.tokenize(doc.get_doc_text()))
                # remove all punctuation
                doc.set_process_text_tokenized(nltkService.NltkService.remove_punctuation_tokenize(doc.get_doc_text()))
                # tokenized text to lower case
                doc.set_process_text_tokenized(nltkService.NltkService.to_lower_case(
                    doc.get_processed_text_tokenized()))
                # remove stop words (using doc tokenized with no punctuation)
                doc.set_text_tokenized_no_stop_words(
                    nltkService.NltkService.remove_stop_words(doc.get_processed_text_tokenized()))
                # find the n number of top terms in the document
                doc.set_top_terms(
                    nltkService.NltkService.most_common(doc.get_text_tokenized_no_stop_words(), doc.get_top_term_count()))
            else:
                raise ValueError('Text from document was null')
    if doc.get_top_terms() is not None:
        if len(doc.get_top_terms()) is not 0:
            return json.dumps(doc.get_top_terms())
        else:
            return None
    return None



if __name__ == "__main__":
    app.debug = True  # Comment this out when going into production
    app.run()
