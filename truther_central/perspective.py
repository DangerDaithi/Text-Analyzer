from truther_central import subjectivity
from truther_central import objectivity
from truther_central import naiveBayesClassifier


class Perspective:
    """
        perspective.py
        This class contains general methods and properties related to a real world perspective
    """

    def __init__(self):
        self.objectivity = objectivity.Objectivity()  # a perspective has objectivity
        self.subjectivity = subjectivity.Subjectivity()  # a perspective has subjectivity
        self.weighted_score = 0  # the weighted score of objectivity and subjectivity scores
        # instance of NaiveBayesClassifier Class
        self.naiveBayesClassifier = naiveBayesClassifier.NaiveBayesClassifier()

    def get_weighted_score(self) -> float:
        """
        Gets the weighted 'perspective' score
        :return: overall weighted/ "truth" score of the perspective
        """
        return self.weighted_score

    def set_weighted_score(self, new_score: float):
        """
        Sets the weighted 'perspective' score
        :param: new_score
        """
        self.weighted_score = new_score
