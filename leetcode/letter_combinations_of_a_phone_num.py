import itertools
def letter_combinations_of_phone(digits):
    DIGIT_LETTERS = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    letters = [DIGIT_LETTERS[d] for d in digits]
    return set(["".join(i) for i in itertools.product(*letters)])

assert(letter_combinations_of_phone("23") == set(["ad", "ae", "af", "bd", 
    "be", "bf", "cd", "ce", "cf"]))