# 3. (15 points) Write a Python function `wordCount(t)` which retrives data in a text file _t_ 
# and returns a dictionary where the _keys_ are unique words in the files and the corresponding
# _values_ are lists of line numbers where the words are found in the text.

f = open('q3.txt', 'r')
content = f.read() 

def wordCount(t):
    words = {}
    count = 0
    for line in t.split('\n'):
        count += 1
        line_words = line.split()
        for word in line_words:
            if word in words:
                words[word].append(count)
            else:
                words[word] = [count]
    print(words)

wordCount(content)
