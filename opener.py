import pickle

pickle_file = open("data/data 2025-05-20 0.json", "rb")
print(pickle.load(pickle_file))