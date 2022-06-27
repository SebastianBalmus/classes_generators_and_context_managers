class ListCreator:
    """Class that manipulates a list"""

    def __init__(self, elements=None):
        if elements is None:
            elements = []
        self.elements = elements

    def set_list(self, elements):
        """Setter"""
        self.elements = elements

    def get_list(self):
        """Getter"""
        return self.elements

    @classmethod
    def from_string(cls, string_list):
        """Convert a string of elements to a list"""
        return ListCreator(list(string_list.split(' ')))

    @staticmethod
    def from_two_lists(first_list, second_list):
        """Merge two lists"""
        return ListCreator(first_list + second_list)
