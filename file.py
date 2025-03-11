class OpenFile:
    """A class to open and close files using a context manager.

    This class provides methods to open and close files safely using the `with` statement.
    It ensures that the file is properly closed even if an exception occurs.
    """
    
    def __init__(self, file_path, mode='r'):
        """Initializes the context for opening a file.

        Args:
            file_path (str): The path of the file to be opened.
            mode (str, optional): The mode in which the file is opened. Defaults to 'r' (read).
        """

        self.file_path = file_path
        self.mode = mode
        self.file = None

    def __enter__(self):
        """Opens the file and returns it for use within the `with` block.

        Returns:
            file: The opened file object.
        """

        self.file = open(self.file_path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Closes the file when exiting the `with` block or due to an exception.

        Args:
            exc_type (type): The type of exception if one occurred.
            exc_val (Exception): The exception instance if one occurred.
            exc_tb (traceback): The traceback object if an exception occurred.
        """
        
        self.file.close()

        if exc_type is not None:
            print(f"An exception occurred: {exc_type} - {exc_val}")
            
class FileProcesses:
    """A class to process a file that has been opened.

    This class processes the file line by line, assuming it is a txt file where each line
    represents attributes of an object.
    """

    def __init__(self, file):
        """Initializes the ProcessFile class with the opened file.

        Args:
            file (file object): The file object to be processed.
        """
        self.file = file

    def get_process(self):
        """Processes the file line by line.

        Each line is assumed to be a txt format, and the attributes are extracted and used
        to create an object or perform some other processing.
        """
        attributes = []
        for line in self.file:
            attributes.append(line.strip().split(',')) 
            
        return attributes
