import pickle
import os

encode_file = "encodings/encodings.pickle"

with open(encode_file,'rb') as rfp:
        existing_encodes = pickle.load(rfp)
        print(existing_encodes)
