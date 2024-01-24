"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """Initializes a new instance of generator"""
        self.count = 0
        self.start = start

    def __repr__(self):
        """String representation of SerialGenerator instance"""
        return f"<SerialGenerator start={self.start} count={self.count}>"


    def generate(self):
        """Saves sum of start and count to num, then adds one to count, then returns num"""
        num = self.start + self.count
        self.count += 1
        return num
    
    def reset(self):
        """Resets count to zero"""
        self.count = 0


    