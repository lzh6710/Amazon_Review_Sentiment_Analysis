#!/usr/bin/env python

import re
import sys

splitter = re.compile('\s+')
nonword_pattern = re.compile(r'[^a-zA-Z]')

def get_word_freq(text):
  word_freq = {};
  max_term_freq = 0
  words = splitter.split(text)
  for word in words:
    word = word.lower()
    if word != '':
      if word in word_freq:
        word_freq[word] += 1
      else:
        word_freq[word] = 1
      if word_freq[word] > max_term_freq:
        max_term_freq = word_freq[word]
  return word_freq, max_term_freq

review = {}

for line in sys.stdin:
  
  line = line.strip()
  key, value = line.split(': ', 1)

  review[key] = value

  if key == 'review/text':
    words = re.sub(nonword_pattern, ' ', value)
    word_freq, max_term_freq = get_word_freq(words)
    
    for word in word_freq:
      # emit word, rating, ntf, and frequency
      print '%s\t%s\t%s\t%s' % (word, review['review/score'], word_freq[word] / float(max_term_freq), word_freq[word])
    review = {}


