class Subjectivity:
    """
        subjectivity class
        a subjective perspective
    """

    def __init__(self):
        self.score = 0

    def get_score(self) -> float:
        """
        Get the subjectivity score for a document
        :return: subjectivity score
        """
        return self.score

    def set_score(self, new_score: float):
        """
        Sets the subjectivity score for the document
        :param new_score: new subjectivity score
        """
        self.score = new_score
