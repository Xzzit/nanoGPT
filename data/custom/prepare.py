import os
import requests
import tiktoken
import numpy as np
import sys
import shutil


# source txt path, /Downloads/filename
#txt_file_path = sys.argv[1]
#print(txt_file_path)
##proj root
#proj_root = '/mnt/barracuda/nanoGPT'
#print(proj_root)
#home dir
#home = os.path.expanduser( '~' )
#print(home)

# copy txt to proj root repo
#src = os.path.join(home, txt_file_path)
#print(src)
#dst = os.path.join(proj_root, txt_file_path.rsplit('/', 1)[-1])
#print(dst)
#shutil.copyfile(src, dst)

# download the tiny essay dataset
input_file_path = sys.argv[1]
print(input_file_path)
with open(input_file_path, 'r') as f:
    data = f.read()
n = len(data)
train_data = data[:int(n*0.9)]
val_data = data[int(n*0.9):]

# encode with tiktoken gpt2 bpe
enc = tiktoken.get_encoding("gpt2")
train_ids = enc.encode_ordinary(train_data)
val_ids = enc.encode_ordinary(val_data)
print(f"train has {len(train_ids):,} tokens")
print(f"val has {len(val_ids):,} tokens")

# export to bin files
train_ids = np.array(train_ids, dtype=np.uint16)
val_ids = np.array(val_ids, dtype=np.uint16)
train_ids.tofile(os.path.join(os.path.dirname(__file__), 'train.bin'))
val_ids.tofile(os.path.join(os.path.dirname(__file__), 'val.bin'))

# train.bin has 301,966 tokens
# val.bin has 36,059 tokens
