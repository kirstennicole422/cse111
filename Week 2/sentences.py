import random

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".
    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
         words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Randomly chooses and returns a noun. If quantity is one it will return a single noun. Otherwise, it will return a plural noun.
    Parameter: quantity- determines singular/plural noun
    Return string of randomly selected noun"""
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    word = random.choice(words)
    return word

def get_verb(quantity, tense):
    """Randomly chooses and returns a noun matching tense and quantity for subject-verb agreement.
    Parameters: quantity- determines singular/plural verb
                tense- determines verb conjugation "past", "present", or "future" """
    if tense.lower() == "past":
        words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense.lower() == "present" and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense.lower() == "present" and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    else:
        words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", 
                 "will talk", "will walk", "will write"]
    word = random.choice(words)
    return word

def get_preposition():
    """Randomly chooses and returns a preposition from a given list"""
    words = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond",
                    "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out",
                     "over", "past", "to", "under", "with", "without"]
    word = random.choice(words)
    return word

def get_prepositional_phrase(quantity):
    """Builds a prepositional phrase with preposition, determiner and noun
    Parameter: quantity- integer determining if noun is singular or plural
    Return: prepositional phrase"""

    phrase = get_preposition() + " " + get_determiner(quantity) + " " + get_noun(quantity)
    return phrase

def make_sentence(quantity, tense):
    """Builds and returns a 5 part sentence. Determiner, noun, verb and prepositional phrase. Grammatical quantity of the noun and verb will 
    match the quantity parameter and the verb tense will match the tense parameter.
    Parameters: quantity - number for single or plural
                tense: "past", "present", or "future" """
    sentence = get_determiner(quantity).title() + " " + get_noun(quantity) + " " + get_prepositional_phrase(quantity) + " " + get_verb(quantity, tense) + " " + get_prepositional_phrase(quantity) + "."
    return sentence

def main():
    print(make_sentence(1, "past"))
    print(make_sentence(1, "present"))
    print(make_sentence(1, "future"))
    print(make_sentence(2, "past"))
    print(make_sentence(2, "present"))
    print(make_sentence(2, "future"))

main()