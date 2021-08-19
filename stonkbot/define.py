from PyDictionary import PyDictionary

dictionary=PyDictionary()

def define(permuatations):
    true_words = []
    for i in tqdm(permuatations):
        if dictionary.meaning(i, disable_errors=True) != None:
            true_words.append(i)
    return true_words

if __name__ == "__main__":
    pass