import random

# x = random.randrange(1,69);
#
# luckyNums = [0,0,0,0,0,0]
#
# luckyNums.insert(0,x)
#
# print(x)
#
# for i in range(4):
#     x = random.randrange(1, 69);


#print(luckyNums)

luckyNumbers = []

for i in range(0,5):
    whiteball = random.randint(1,69)
    # if the number is in the list. do while loop again until the number is not in the list
    while whiteball in luckyNumbers:
        luckyNum = random.randint(1,69)
    luckyNumbers.append(whiteball)
# sort the 5 lucky numbers
luckyNumbers.sort()
# redball does not need to be sorted.
redball = random.randint(1,26)
luckyNumbers.insert(6,redball)
print("Hi, your lucky numbers for the week are: ")
print(luckyNumbers)
print("Please play responsibly")
print("If you have a gambling addiction please call the National Problem Gambling Helpline Network's phone number at 1-800-522-4700")
print("Help is available 24/7 and is 100% confidential.")
print("The National Problem Gambling Helpline Network also includes text and chat services.")