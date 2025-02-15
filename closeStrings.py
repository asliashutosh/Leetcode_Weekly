def closeStrings(self, word1: str, word2: str) -> bool:
    """
    Determines whether two strings are 'close' based on the following conditions:
    1. They must have the same set of unique characters.
    2. The frequency counts of characters must be rearrangeable (i.e., they can be swapped but should match).

    Parameters:
    - word1: First input string
    - word2: Second input string

    Returns:
    - True if the words are 'close', otherwise False
    """

    # If lengths are different, they can never be close
    if len(word1) != len(word2):
        return False

    # Dictionaries to count occurrences of each character in both words
    dict1 = {}
    dict2 = {}

    # Dictionaries to count the frequency of character occurrences
    freq_counter1 = {}
    freq_counter2 = {}

    # Step 1: Build character frequency dictionaries for both words
    for i in range(len(word1)):
        dict1[word1[i]] = dict1.get(word1[i], 0) + 1
        dict2[word2[i]] = dict2.get(word2[i], 0) + 1

    # Step 2: Both words must have the exact same set of characters
    if dict1.keys() != dict2.keys():
        return False

    # Step 3: Count the occurrences of each frequency value
    # Example: If a word has 'a' appearing 3 times, we store count 3 in freq_counter
    for freq1, freq2 in zip(dict1.values(), dict2.values()):
        freq_counter1[freq1] = freq_counter1.get(freq1, 0) + 1
        freq_counter2[freq2] = freq_counter2.get(freq2, 0) + 1

    # Step 4: The frequency counts should be identical (order doesn't matter)
    return freq_counter1 == freq_counter2
