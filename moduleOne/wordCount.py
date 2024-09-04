"""read file from web and do analysis
of data
"""

from urllib.request import urlopen

def countWordsFromFile(URL):
    """gets and counts number of words from file from web

    Args:
        URL (str): a str of a web url
    """
    with urlopen(URL) as data:
        words = 0
        for line in data:
            #print(line, type(line))
            line = line.decode('utf-8') # converts bytes to strings
            #print(line.decode('utf-8', type(line)))
            line_words = line.split()
            for word in line_words:
                words += 1

    return words

def main():
    """Driven Function
    """
    file_address = 'http://icarus.cs.weber.edu?~hvalle/sample_data/poem.txt'
    words = countWordsFromFile(file_address)
   



if __name__ == '__main__':
    main()