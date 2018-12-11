import urllib.request
import gzip
import struct

'''
The MNIST database of handwritten digits, available from this page, has a training set 
of 60,000 examples, and a test set of 10,000 examples. It is a subset of a larger set 
available from NIST. The digits have been size-normalized and centered in a fixed-size image.
'''

train_images_url = 'http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz'
train_labels_url = 'http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz'
test_images_url = 'http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz'
test_labels_url = 'http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz'

# data = response.read()


# %%
response = urllib.request.urlopen(test_labels_url)
unzipped = gzip.open(response)
magic, count = struct.unpack('>ii', unzipped.read(8))
data = [struct.unpack('B', unzipped.read(1))[0] for _ in range(count)]
unzipped.close()

# %%

data = unzipped.read()
print(len(data))

# %%
