from random import choice

def primary():

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    print(choice(quotes))

if __name__== "__main__":
  primary()
