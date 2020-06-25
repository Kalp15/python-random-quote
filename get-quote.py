import random
def primary():
  # print("Keep it logically awesome.")
  list = 13
  ran = random.randint(0,list)
  
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[ran])

if __name__== "__main__":
  primary()
