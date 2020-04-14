#!/usr/bin/python3.5
import sys
from urllib.request import urlopen

def fetch_words(url):
    #story = urlopen('https://raw.githubusercontent.com/elmanko/python101/master/README.md') #la url estaba hardcodeada, la hice argumento, e importe sys para los argumentos
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


'''
def print_words(story_words):
    for word in story_words:
        print(word)
'''
# la misma funcion nomas que refleja que jala items no words por que lvv si es string o integer
def print_items(items):
    for item in items:
        print(item)

def main(url):
    words = fetch_words(url)
    print_items(words)
    #print_words(words)
     

if __name__ == '__main__':
    main(sys.argv[1])
