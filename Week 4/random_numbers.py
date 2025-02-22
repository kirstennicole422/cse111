import random
# import math

def append_random_numbers(numbers_list, quantity = 1):
    for x in range(quantity):
        new_number = random.uniform(0,100)
        new_number = round(new_number,1)
        numbers_list.append(new_number)

def append_random_words(words_list, quantity = 1):
    word_list = ["dog", "cat", "tree", "hat", "bat", "log", "plant", "mouse", "elephant"]
    for x in range(quantity):
        new_word = words_list(random)
        words_list.append(new_word)

def main():
    numbers = [16.2, 75.1, 52.3]
    print(numbers)
    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers, 3)
    print(numbers)
    words = ["hat", "fish", "bat"]
    append_random_words (words, 3)
main()