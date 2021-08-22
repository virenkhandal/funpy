from PyDictionary import PyDictionary
import itertools
from tqdm import tqdm
from define import *
from utils import *
dictionary=PyDictionary()

def permute(scramble):
    letters = []
    possible_words = []
    for i in scramble:
        letters.append(i)
    for k in range(3,len(letters)):
        subset = letters[k:]
        permutations = itertools.permutations(subset)
        print(permutations)
        for j in permutations:
            possible_words.append(''.join(map(str, j)))
    print("found all possible words... defining ...")
    return possible_words

# def define(permuatations):
#     true_words = []
#     for i in tqdm(permuatations):
#         if dictionary.meaning(i, disable_errors=True) != None:
#             true_words.append(i)
#     return true_words



if __name__ == "__main__":
    scramble = input("Enter the letters from your puzzle: ")
    permuatations = permute(scramble)
    words = definition(permuatations)
    pretty_print(words)
