"""Word Finder: finds random words from a dictionary."""

from random import choice

class WordFinder:
    """
    A machine to parse a text file, return the number of words in the file, and optionally generate a random word from the file.

    >>> wf = WordFinder("example.txt")
    3 words read

    >>> wf.random() in ['cat', 'dog', 'porcupine']
    True
    """

    def __init__(self, filepath):
        """Initializes a new instance of WordFinder"""
        self.filepath = filepath
        self.parse_file() 
        self.print_len()
    
    def parse_file(self):
        """Parses words from text file into a list"""
        self.words = []
        file = open(self.filepath, 'r')
        for line in file:
            self.words.append(line.strip())
        file.close()

    def print_len(self):
        """Prints the length of the list"""
        print(f"{len(self.words)} words read")

    def random(self):
        """Returns a random word from the list"""
        return(choice(self.words))


class SpecialWordFinder(WordFinder):
    """    
    A machine to parse a text file, return the number of words in the file while ignoring words that do not start with a letter, and optionally generate a random word from the file.

    >>> swf = SpecialWordFinder("special.txt")
    4 words read

    >>> swf.random() in ['kale', 'parsnips', 'apple', 'mango']
    True
    """

    def __init__(self, filepath):
        """Initializes a new instance of SpecialWordFinder"""
        self.filepath = filepath 
        self.special_parse()
        super().print_len()
    
    def special_parse(self):
        """Parses words from text file into a list while ignoring words that do not start with a letter"""
        self.words = []
        file = open(self.filepath, 'r')
        for line in file:
            if line[0].isalpha():
                self.words.append(line.strip())
        file.close()
    

