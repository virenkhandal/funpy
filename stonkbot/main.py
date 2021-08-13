from PyDictionary import PyDictionary
import itertools
from termcolor import colored
from tqdm import tqdm

dictionary=PyDictionary()

def permute(scramble):
    letters = []
    possible_words = []
    for i in scramble:
        letters.append(i)
    permutations = itertools.permutations(letters)
    for j in permutations:
        possible_words.append(''.join(map(str, j)))
    print("found all possible words... defining ...")
    return possible_words

def define(permuatations):
    true_words = []
    for i in tqdm(permuatations):
        if dictionary.meaning(i, disable_errors=True) != None:
            true_words.append(i)
    return true_words

def pretty_print(words):
    print("\n")
    for word in words:
        # print(colored(word, "grey", "on_green"))
        print(word)
        print("\n")

if __name__ == "__main__":
    scramble = input("Enter the letters from your puzzle: ")
    permuatations = permute(scramble)
    words = define(permuatations)
    pretty_print(words)
