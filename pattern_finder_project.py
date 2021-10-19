"""
 A class for a pattern in ASCII format
"""

class PatternFinder:

    # Initialised from a text file with the ASCII style drawing.
    # Store the coordinates and values (i.e. character that corresponds to these coordinates)

    def __init__(self, bug_file, landscape_file):
        self.bug_content = {}
        self.landscape_content = {}

        self.read_file_content(bug_file, self.bug_content)
        self.read_file_content(landscape_file, self.landscape_content)

        self.get_bug_pattern()

    def read_file_content(self, file, content):
        with open(file, 'r') as f:
            y = 0
            for line in f:
                x = 0
                for char in line.rstrip():
                    if char != ' ':
                        content[(x, y)] = char
                    x += 1
                y += 1

    """
    The Bug has specific methods.
    The first occurence of a relevant character in the read direction (up/down, left/right)
    is the anchor, or local origin.
    We find it and then recalculate all coordinates such that the origin is always at (0, 0)
    """
    def get_bug_pattern(self):
        # The first occurrence of a char in the read direction (up/down, left/right) is the anchor
        anchor = None

        for coord, char in self.bug_content.items():
            if (
                    anchor is None
                    or coord[1] < anchor[1]
                    or (coord[1] == anchor[1] and coord[0] < anchor[0])
            ):
                anchor = coord

        # Reallocate all coordinates to have anchor always at (0, 0)
        reallocated_content = {}
        for coord, char in self.bug_content.items():
            x = coord[0] - anchor[0]
            y = coord[1] - anchor[1]
            reallocated_content[(x, y)] = char
        self.bug_content = reallocated_content

    def bug_match_all(self, start):
        """
        Match all relevant chars with the given landscape at the given position
        :param start:
        :return:
        """
        # Find if all char after the fist match are the same that in the pattern
        for bug_coord, char in self.bug_content.items():
            # Transform bug coordinates to landscape coordinates:
            landscape_x = start[0] + bug_coord[0]
            landscape_y = start[1] + bug_coord[1]
            if not self.landscape_check_char_at((landscape_x, landscape_y), char):
                return False
        return True

    def count_pattern_occurrences(self):
        """Count the own pattern occurences in the given landscape"""
        occurrences = 0
        # First we match the origin:
        for start in self.landscape_first_matches(self.bug_content[(0, 0)]):
            """find the char in the landscape that is equal to the first char in the pattern(bug)
             We verify if the following matches are the same that the pattern,
             if True we count a occurrence 
             """
            if self.bug_match_all(start):
                occurrences += 1
        return occurrences

    def landscape_first_matches(self, char):
        """
        Generate the coordinates that match a given char
        :param char:
        :return:
        """
        for coord, c in self.landscape_content.items():
            if c == char:
                yield coord

    def landscape_check_char_at(self, coord, char):
        """
        Check the existence of a given char at the given coordinate
        :param coord:
        :param char:
        :return:
        """
        return coord in self.landscape_content and self.landscape_content[coord] == char


def test_pattern_finder(bug_file_name, landscape_file_name, expected):
    finder = PatternFinder(bug_file_name, landscape_file_name)
    pattern_count = finder.count_pattern_occurrences()

    assert pattern_count == expected
    print(f'The number of occurrences: {pattern_count} is correct')


parameters = [
    ('bug.txt', 'bug.txt', 1),
    ('bug.txt', 'landscape.txt', 3),
    ('bug.txt', 'landscape_test1.txt', 3)
]


for bug_file_name, landscape_file_name, expected  in parameters:
    test_pattern_finder(bug_file_name, landscape_file_name, expected)