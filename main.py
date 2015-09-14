import csv
import random
import sys

def read_words_file(filename):
    words = []
    f = open(filename)
    csv_f = csv.reader(f)

    for row in csv_f:
        words.append((row[0],row[1]))

    f.close()

    return words


def quiz_words(words):
    while len(words) > 0:
        random.shuffle(words)
        for w in words:
            print("{} ".format(w[0]))
            input = str(sys.stdin.readline())[:-1]
            if input == w[1]:
                words.remove(w)
                print("Correct. {} words remainig".format(len(words)))
            else:
                print("Wrong. The correct answer is \"{}\"".format(w[1]))




def main():
    if len(sys.argv) < 2:
        print("Usage: {} <wordsfile>".format(sys.argv[0]))
        return
    words = read_words_file("svenska01")
    

    quiz_words(words)

if __name__ == "__main__":
    main()
