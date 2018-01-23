#----------------------------------------------------------------
#  Author:        Rodney Greene
#  Written:       1/22/2018
#  Last updated:  1/22/2018
#
#  Compilation:   WordCounter.py
#  Execution:     Python WordCounter
#  
#  Counts occurances of unique words in a string.
#
#	python WordCounter.py
#----------------------------------------------------------------


import re

def word_count(str):
    counts = dict()
    words = re.split(r'[^\w]', str)

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    print(counts)

word_count('word')											#should print out 'word': 1

word_count('one of each')          							#should print out  'one': 1, 'of': 1, 'each': 1

word_count('one fish two fish red fish blue fish')  		#should print out  'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1

word_count('one,two,three')                         		#should print out  'one': 1, 'two': 1, 'three': 1

word_count('one,\ntwo,\nthree')                     		#should print out  'one': 1, 'two': 1, 'three': 1
            
word_count('car : carpet as java : javascript!!&@$%^&')    	#should print out  'car': 1, 'carpet': 1, 'as': 1, 'java': 1, 'javascript': 1

word_count('testing 1 2 testing')                 			#should print out 'testing': 2, '1': 1, '2': 1

word_count('go Go GO Stop stop')                  			#should print out  'go': 3, 'stop': 2

word_count("First: don't laugh. Then: don't cry.")      	#should print out  'first': 1, "don't": 2, 'laugh': 1, 'then': 1, 'cry': 1

word_count("Joe can't tell between 'large' and large.")    	#should print out  'joe': 1, "can't": 1, 'tell': 1, 'between': 1, 'large': 2,             'and': 1

word_count('wait for       it')                      		#should print out  'wait': 1, 'for': 1, 'it': 1