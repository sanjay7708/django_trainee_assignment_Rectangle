class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        self._attributes = [
            {'length': self.length},
            {'width': self.width}
        ]
        self._index = 0  # To keep track of iteration

    # Defining the __iter__ method to return the iterator object
    def __iter__(self):
        self._index = 0  # Reset index for fresh iteration
        return self

    # Defining the __next__ method to return the next item
    def __next__(self):
        if self._index < len(self._attributes):
            result = self._attributes[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration  # End the iteration

# Example usage
rect = Rectangle(10, 5)

# Iterating over the rectangle object
for attr in rect:
    print(attr)

