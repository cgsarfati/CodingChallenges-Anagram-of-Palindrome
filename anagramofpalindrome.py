"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    # put letters in dictionary with k(word):v(count)
    # extract all count values w/ .values()
    # if any of values are odd more than once (1 occurence is ok to account
    # for odd-numbered word) --> if so, return False

    # EDGE CASE: 2-LETTER WORD
    if len(word) == 2:
        if word[0] != word[1]:
            return False
        else:
            return True  # win fast method vs. continuing w/ rest of code

    # obtain dict with k(letter):v(count) pairs
    letter_count = {}

    for letter in word:
        letter_count[letter] = letter_count.get(letter, 0) + 1

    # establish counting mechanism; if odd, +=1. If var > 1: return False
    odd_number = 0

    for count in letter_count.values():
        if count % 2 != 0:
            odd_number += 1
        if odd_number >= 2:
            return False

    return True

    # RUNTIME: O(N)

if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"
