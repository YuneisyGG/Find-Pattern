# Find Pattern project


This project provides a implementation that search for a bug in a text file and print the number of occurences. 


### Requirements:

- Python 2.*

### Implementation:

To implement this project, we created the main class called: PatternFinder, which has different methods that allow us to identify the bug. For doing so, we first identify the pattern of the bug in the bug.txt file and then look for the occurrences of the same pattern in the lanscape.txt file.

Methods:

- read_file_content: allows to read a text file and extract the coordinates of each character. (This allows to identify the pattern that is in the bug.txt file)
- get_bug_pattern: allows to find the first occurrence of a character in a bug.txt file and reallocate all coordinates such that they have anchor always at (0, 0)
- bug_match_all: checks if after the first identify character in the landscape.txt, all the following characters match the pattern of the bug. 
- count_pattern_occurrences: counts the number of occurrences of the pattern in the landscape 
- landscape_first_matches: finds the position of the first character of the pattern of the bug in the landscape
- landscape_check_char_at: checks the existence of a given character at the given coordinate

### Testing

Finaly we have a "test_pattern_finder" method that allow to check different test cases with different txt files.


### Author:

-Yuneisy G. G 


