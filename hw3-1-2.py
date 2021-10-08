#Author: JTI 9/28/21

card_1 = input("Enter 1st card: ")
card_2 = input("Enter 2nd card: ")

total = int(card_1) + int(card_2)
if total < 21:
  print("safe")
else:
  print("busted")
