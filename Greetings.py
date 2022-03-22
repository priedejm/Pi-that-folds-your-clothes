# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
import random

#geezz python has such simplictly syntax which makes it so diffcult in some cases. HOW DO YOU RUN THE MAIN FUNCTION


def main():
    #4 buttons when press will do one of each of these
    print("Welcome to the pi that will fold your cloths for you\nWhat would you like to do?")
    print("1)Fold cloth\n2)My stats\n3)Today's lucky numbers\n4)A joke")

    userInput = input()

    if int(userInput) == 1:
        print("Hi there 1")
        #more code coming
        foldClothFunction()
    elif int(userInput) == 2:
        print("Hi there 2")
        #more code coming
        myStatsFuntion()
    elif int(userInput) == 3:
        print("Hi there 3")
        #more code coming
        luckyNumsFunction()
    elif int(userInput) == 4:
        print("Hi there 4")
        #more code coming
        aJokeFunction()
    else:
        print("Error: getting input from user stage")




def foldClothFunction():
    print()
    #will go into this function doing some cool stuff with more options
def myStatsFuntion():
    print()
    #have some kind of backend to keep track of fun states
def luckyNumsFunction():
    print()
    #go to the luckyNums file.py


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

    # print(luckyNums)
    luckyNumAgain = 0
    while luckyNumAgain == 0:
        luckyNumbers = []

        for i in range(0, 5):
            whiteball = random.randint(1, 69)
            # if the number is in the list. do while loop again until the number is not in the list
            while whiteball in luckyNumbers:
                luckyNum = random.randint(1, 69)
            luckyNumbers.append(whiteball)
        # sort the 5 lucky numbers
        luckyNumbers.sort()
        # redball does not need to be sorted.
        redball = random.randint(1, 26)
        luckyNumbers.insert(6, redball)
        print("Hi, your lucky numbers for the week are: ")
        print(luckyNumbers)
        print("Please play responsibly")
        print(
            "If you have a gambling addiction please call the National Problem Gambling Helpline Network phone number at 1-800-522-4700")
        print("Help is available 24/7 and is 100% confidential.")
        print("The National Problem Gambling Helpline Network also includes text and chat services.")
        print()
        print()
        print("Would you like another set of lucky number? yes or no")
        userinput = input()
        if userinput == "yes":
            luckyNumAgain = 0;
        if userinput == "no":
            main()

def aJokeFunction():
    #going to have 100+ jokes and store them somewhere else.
    #random number generator
    #switch statement....or something
    
    #print(ranNum)
    tellAJokeAgain = 0
    while tellAJokeAgain == 0:
        ranNum = random.randint(1,16)
        if ranNum == 1:
            print("what's a ghost's favourite type?")
            print("Booooolean")
        if ranNum == 2:
            print("student: My dog ate my homework")
            print("Teacher: But it's an online homework")
            print("student: yes, he took quite a byte out of it")
        if ranNum == 3:
            print("There are 10 types of people in this world.\nThose who understand binary and those who don't.")
        if ranNum == 4:
            print("There are 10 types of people in this world.")
            print("Those who understand binary and those who don't.. and those who know this is a trinary joke.")
        if ranNum == 5:
            print("Why did the programmer quit his job?")
            print("because he didn't get arrays")
        if ranNum == 6:
            print("How many software engineer does it take to change a light bulb?")
            print("none, that's a hardware problem")
        if ranNum == 7:
            print("I've got a really good UDP joke to tell you, but I don't think you'll get it")
        if ranNum == 8:
            print("What's the best part about TCP jokes?\nI get to keep telling them until you get them.")
        if ranNum == 9:
            print("A guy walks into a bar and asks for 1.4 root beers. The bartender says \"I'll have to charge you extra, that's a root beer float\".")
            print("The guy says \"In that case, better make it a double.\"")
        if ranNum == 10:
            print("Java and C++ were telling jokes. It was C++'s turn, so he writes something on the wall, points to it and says \"Do you get the reference?\" But Java didn't.")
        if ranNum == 11:
            print("wife: could you pass the salt, dear")
            print("husband: by value or by reference?")
        if ranNum == 12:
            print("In order to understand recursion you must first understand recursion.")
        if ranNum == 13:
            print("how do SQL developer get into their house?\nWith keys")
        if ranNum == 14:
            print("What is a programmers favorite exercise activity?\nSprint")
        if ranNum == 15:
            print("Why do IT people wear glasses\nBecause they don't C#")
        if ranNum == 16:
            print("why was there no windows 9?")
            print("because windows 7 8 9.")
        print("Would you like to hear another joke? yes or no")
        userinput = input()
        if userinput == "yes":
            tellAJokeAgain = 0;
        if userinput == "no":
            main()


main()