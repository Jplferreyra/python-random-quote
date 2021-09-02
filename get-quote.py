from random import choices

def primary():
    f = open("quotes.txt", 'a')
    new_quote = input("For the sake of maintenance, you have to type a new quote: ")
    f.write(f"{new_quote}\n")
    f.close()
    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    quantity = int(input('How many quotes do you want to see? '))
    rndm_choices = choices(quotes, k=quantity)
    for q in rndm_choices:
        print(q.strip())

if __name__== "__main__":
  primary()
