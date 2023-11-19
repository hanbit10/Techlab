import numpy as np # linear algebra
import struct
from os.path  import join
import gzip
import urllib.request
from os import path
import os
import array

def _partial_flatten(x):
    return np.reshape(x, (x.shape[0], -1))

def _one_hot( x, k, dtype=np.float32):
    return np.array(x[:, None] == np.arange(k), dtype)


def download(url, filename, data_dir="./data/datasets"):
    """Download a url to a file in the JAX data temp directory."""
    if not path.exists(data_dir):
        os.makedirs(data_dir)
    out_file = path.join(data_dir, filename)
    if not path.isfile(out_file):
        urllib.request.urlretrieve(url, out_file)
        print(f"downloaded {url} to {data_dir}")

def load_data(base_path):
    base_url = "https://storage.googleapis.com/cvdf-datasets/mnist/"

    def parse_labels(filename):
        with gzip.open(filename, "rb") as fh:
            _ = struct.unpack(">II", fh.read(8)) #type: ignore
            return np.array(array.array("B", fh.read()), dtype=np.uint8) #type: ignore

    def parse_images(filename):
        with gzip.open(filename, "rb") as fh:
            _, num_data, rows, cols = struct.unpack(">IIII", fh.read(16)) #type: ignore
            return np.array(array.array("B", fh.read()), #type: ignore
                        dtype=np.uint8).reshape(num_data, rows, cols)

    
    for filename in ["train-images-idx3-ubyte.gz", "train-labels-idx1-ubyte.gz",
                   "t10k-images-idx3-ubyte.gz", "t10k-labels-idx1-ubyte.gz"]:
        download(base_url + filename, filename, base_path)

    x_train = parse_images(path.join(base_path, "train-images-idx3-ubyte.gz"))
    y_train = parse_labels(path.join(base_path, "train-labels-idx1-ubyte.gz"))
    x_test = parse_images(path.join(base_path, "t10k-images-idx3-ubyte.gz"))
    y_test = parse_labels(path.join(base_path, "t10k-labels-idx1-ubyte.gz"))

    return x_train, y_train, x_test, y_test

def transform_data(x_train, y_train, x_test, y_test):

    x_train = _partial_flatten(x_train) / np.float32(255.)
    x_test = _partial_flatten(x_test) / np.float32(255.) 
    y_train = _one_hot(y_train, 10)
    y_test = _one_hot(y_test, 10)

    return x_train, y_train, x_test, y_test
