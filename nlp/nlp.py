import gensim
from gensim.models import Word2Vec, KeyedVectors

model = gensim.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True, limit=100000)

model.wv.most_similar('man')