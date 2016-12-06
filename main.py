from __future__ import absolute_import, division, print_function

import os
import pickle
from six.moves import urllib

import tflearn
from tflearn.data_utils import *

path = "lotr_data.txt"
char_idx_file = 'char_idx.pickle'

# Change to path of my own github folder
#if not os.path.isfile(path):
#    urllib.request.urlretrieve("https://raw.githubusercontent.com/tflearn/tflearn.github.io/master/resources/shakespeare_input.txt", path)

maxlen = 25

char_idx = None
if os.path.isfile(char_idx_file):
  print('Loading previous char_idx')
  char_idx = pickle.load(open(char_idx_file, 'rb'))

X, Y, char_idx = \
    textfile_to_semi_redundant_sequences(path, seq_maxlen=maxlen, redun_step=10)

pickle.dump(char_idx, open(char_idx_file,'wb'))

g = tflearn.input_data([None, maxlen, len(char_idx)])
g = tflearn.lstm(g, 128, return_seq=True)
g = tflearn.dropout(g, 0.5)
g = tflearn.lstm(g, 128, return_seq=True)
g = tflearn.dropout(g, 0.5)
g = tflearn.lstm(g, 128)
g = tflearn.dropout(g, 0.5)
g = tflearn.fully_connected(g, len(char_idx), activation='softmax')
g = tflearn.regression(g, optimizer='adam', loss='categorical_crossentropy',
                       learning_rate=0.001)

m = tflearn.SequenceGenerator(g, dictionary=char_idx,
                              seq_maxlen=maxlen,
                              clip_gradients=5.0,
                              checkpoint_path='model_lotr')

#for i in range(1):
seed = random_sequence_from_textfile(path, maxlen)
m.fit(X, Y, validation_set=0.1, batch_size=128,
      n_epoch=1, run_id='lotr')

# Create ten sentences and add them to the list.
the_awesome_lotr_sentences_file = open('the_awesome_lotr_sentences_file.txt', 'w')

for i in range(10):
  # I dare you to watch this video and then read the variable below without laughing
  # https://www.youtube.com/watch?v=9U2pINNSpHE
  gandaalfff = m.generate(600, temperature=1.0, seq_seed=seed) #random sentence
  the_awesome_lotr_sentences_file.write("\r%s\n" % gandaalfff)
  print('GANDALLFFFFF sentence: ' + i)