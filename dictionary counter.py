fw= open('sample.txt', 'w')
fw.write('My dear fellow citizens,The whole world is currently passing through a period of very serious crisis. Normally, when a natural crisis strikes, it is limited to a few countries or states. However, this time the calamityis such that it has it has put all of mankind in crisis. World Wars 1 and 2 did not impact as many countries, as have been affected by Corona today.')
fw.close()
fr = open('sample.txt', 'r')
operation = fr.read()
print(operation)
counts = dict()
for word in operation:
    words = word.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

words_count = 0
max_word = 0
for word,count in counts.items():
    if max_word is None or count > words_count:
        max_word = word
        words_count = count
print(words_count,max_word)