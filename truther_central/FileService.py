class FileService:
    """
        FileService.py
        This class contains general utilities for reading and writing to external data sources
        such as .txt and .csv files
    """

    @staticmethod
    def read_file(file_path: str):
        """
            Read file from given file_path argument, and return text read from file
            :param file_path: string representing the location of the file to read from
            :return: string "text" containing the text from the file
        """

        # try and read from the file
        try:
            file = open(file_path, 'r', encoding='utf8', errors='ignore')
            text = file.read()
            return text
        except IOError:
            print('Error reading file')

        # handle exception return null
        return None
