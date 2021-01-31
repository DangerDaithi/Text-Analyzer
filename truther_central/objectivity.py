class Objectivity:
    """
        objectivity class
        An objective perspective
    """

    def __init__(self):
        self.score = 0

    def get_score(self) -> int:
        """
        Gets the objectivity score for the document
        :return: objectivity score
        """
        return self.score

    def set_score(self, new_score: int):
        """
        Sets the objectivity score for the document
        :param new_score: new objectivity score
        """
        self.score = new_score
