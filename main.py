#Section A:-
#Even Number 
import pandas as pd

def even_no():
  ask = int(input("Enter length of list : "))
  li=[]
  for i in range(ask):
    num = int(input(f"Enter No. {i+1} : "))
    if isinstance(num, int):
      li.append(num)
    else:
      print(f"{num} is not int number.")
  return [x for x in li if x%2 == 0]

e1 = even_no()
print(e1)

#Char count
def char_count(s:str):
  df={}
  li=s.split(" ")
  for i in range(len(li)):
    if li[i] not in df.keys():
      df[li[i]] = 1
    else:
      df[li[i]] +=1
  return df

char_count("hello my name my is is yoge")

#file reader
def file_reader(path):
    try:
        with open(path, "r") as f:
            data = f.read()
            data_li = data.split(" ")
            #data words count
            print(f"Total words in data = {len(data)}")
            
            #frequent words
            dic = {}
            for word in data_li:
                if word not in dic.keys():
                    dic[word] = 1
                else:
                    dic[word] += 1

            freq_dic = dict(sorted(dic.items(), key= lambda x : x[1], reverse=True))
            df = list(freq_dic.items())[:6]

            for word, freq in df:
              print(f"{word} : {freq}")
    except FileNotFoundError:
        return ("File not found, or Check your path.")

file_reader(fr"D:\New folder\EV_Assigments\EV_Assessment\data.txt")

class BankAccount:
  def __init__(self,account_number,amount) -> None:
     self.account_number = account_number
     self.amount = amount

  def deposit(self,amount):
    if amount > 0:
      self.amount += amount
      return f"Amount {amount} Deposit Success-fully\nCurrent Balance : {self.amount}\n"
    else:
      return "Amount is not appropriate"

  def withdraw(self,amount):
    if amount < self.amount:
      self.amount -= amount
      return f"Amount {amount} Withdraw Success-fully\nCurrent Balance : {self.amount}\n"
    else:
      return f"Sorry you'r current Bank Balance is lower than withdraw amount {amount}!"

  def dispaly(self):
    return f"\nAccount Number : {self.account_number}\nCurrent Balance : {self.amount}"

# obj1 = BankAccount(242333,10000)
# print(obj1.deposit(5000))
# print(obj1.withdraw(12000))
# print(obj1.dispaly())