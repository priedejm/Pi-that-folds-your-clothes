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
from cgitb import text
import random
import re
import array
#geezz python has such simplictly syntax which makes it so diffcult in some cases. HOW DO YOU RUN THE MAIN FUNCTION



def foldClothFunction():
    print()
    #script for start up, and end
    #not completed yet
    #automatic mode
    #touch mode
    keepfolding = True
    while keepfolding == True:
        with open ("dataSheet.txt", "r+") as file:
            dataNum = array.array('i',[0,0,0,0,0,0,0,0])
            dataNum2 = []
            count = 0
            # for line in file:    
            #     #anum = int(re.search(r'\d+', line).group())
            #     #anum = int(file.readline())
            #     dataNum.insert(count,anum)
            # #print(anum)
            #     count += 1
            for num in file.readlines():
                dataNum2.append(int(num))
            print(dataNum2) 
            # for i in range (0, 8):
            #     print (dataNum2[i], end =" ")
            # print()
        file.close()
        print("1 for folding shirts")
        print("2 for folding pants")
        print("3 for folding towels")
        print("4 for main menu")
        typeofFold = int(input())
        if typeofFold == 1:
            #code for folding shirts goses in this if block---------------
            try:
                print("\n");
                print("folding shirts in progress")
                stringNumZero = dataNum2[0] + 1
                stringNum = str(dataNum2[2])
                with open ("dataSheet.txt", "w+") as f:
                    f.write(str(stringNumZero) + "\n") #+ "\n" + stringNum)
                    f.write(str(dataNum2[1]) + "\n")
                    f.write(str(dataNum2[2]) + "\n")
                    f.write(str(dataNum2[3] + 1) + "\n")
                    f.write(str(dataNum2[4] + 1) + "\n")
                    f.write(str(dataNum2[5]) + "\n")
                    f.write(str(dataNum2[6]) + "\n")
                    f.write(str(dataNum2[7] + 1) + "\n")
                    #f.append(stringNum)
                f.close()
                print(dataNum2[0])
                print("done")
            except:
                print("error trying to fold shirts please redo")
                file.close()
                foldClothFunction()
                foldClothFunction()
        if typeofFold == 2:
            #code for folding pants goses in this if block---------------
            try:
                print("\n");
                print("folding pants in progress")
                stringNumZero = str(dataNum2[0])
                dataNum2[1] = dataNum2[1] + 1
                stringNum = str(dataNum2[1])
                with open ("dataSheet.txt", "w+") as f:
                    f.write(stringNumZero + "\n") #+ "\n" + stringNum)
                    f.write(stringNum + "\n")
                    f.write(str(dataNum2[2]) + "\n")
                    f.write(str(dataNum2[3] + 1) + "\n")
                    f.write(str(dataNum2[4]) + "\n")
                    f.write(str(dataNum2[5] + 1) + "\n")
                    f.write(str(dataNum2[6]) + "\n")
                    f.write(str(dataNum2[7] + 1) + "\n")
                    #f.append(stringNum)
                f.close()
                print(dataNum2[0])
                print("done")
            except:
                print("error trying to fold shirt please redo")
                file.close()
                foldClothFunction()
        if typeofFold == 3:
            #code for folding towel goses in this if block---------------
            try:
                print("\n");
                print("folding towls in progress")
                stringNumZero = str(dataNum2[0])
                stringNumOne = str(dataNum2[1])
                dataNum2[2] = dataNum2[2] + 1
                stringNum = str(dataNum2[2])
                with open ("dataSheet.txt", "w+") as f:
                    f.write(stringNumZero + "\n") #+ "\n" + stringNum)
                    f.write(stringNumOne + "\n")
                    f.write(str(dataNum2[2]) + "\n")
                    f.write(str(dataNum2[3] + 1) + "\n")
                    f.write(str(dataNum2[4]) + "\n")
                    f.write(str(dataNum2[5]) + "\n")
                    f.write(str(dataNum2[6] + 1) + "\n")
                    f.write(str(dataNum2[7] + 1) + "\n")
                    #f.append(stringNum)
                f.close()
                print(dataNum2[0])
                print("done")
            except:
                print("error trying to fold towel please redo")
                file.close()
                foldClothFunction()
        if typeofFold == 4:
            keepfolding = False
            break;

        foldClothFunction()
    print("\n");
    file.close()
            
        
        
        
def myStatsFuntion():
    print()
    
    readStatsAgain = 0
    while readStatsAgain == 0:
        with open ("dataSheet.txt", "r") as file:
            var = file.read()
            print(var)
            file.close()
        print("\n");
        print("Would you like to see your stats again? Type: yes or no")
        userinput = input()

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

def aJokeFunction():
    #going to have 100+ jokes and store them somewhere else.
    #random number generator
    #switch statement....or something
        text = ""
    #print(ranNum)
        ranNum = random.randint(1,30)
        if ranNum == 1:
            text =  "what's a ghost's favourite type? \nBooooolean"
        if ranNum == 2:
            text = "student: My dog ate my homework \nTeacher: But it's an online homework \nstudent: yes, he took quite a byte out of it"
        if ranNum == 3:
            text = "There are 10 types of people in this world.\nThose who understand binary and those who don't."
        if ranNum == 4:
            text = "There are 10 types of people in this world. \nThose who understand binary and those who don't.. and those who know this is a trinary joke."
        if ranNum == 5:
            text = "Why did the programmer quit his job? \nbecause he didn't get arrays"
        if ranNum == 6:
            text = "How many software engineer does it take to change a light bulb? \nnone, that's a hardware problem"
        if ranNum == 7:
            text = "I've got a really good UDP joke to tell you, but I don't think you'll get it"
        if ranNum == 8:
            text = "What's the best part about TCP jokes?\nI get to keep telling them until you get them."
        if ranNum == 9:
            text = "A guy walks into a bar and asks for 1.4 root beers. The bartender says \"I'll have to charge you extra, that's a root beer float\". \nThe guy says \"In that case, better make it a double.\" "
        if ranNum == 10:
            text = "Java and C++ were telling jokes. It was C++'s turn, so he writes something on the wall \n points to it and says \"Do you get the reference?\" But Java didn't."
        if ranNum == 11:
            text = "wife: could you pass the salt, dear \nhusband: by value or by reference?"
        if ranNum == 12:
            text = "In order to understand recursion you must first understand recursion."
        if ranNum == 13:
            text = "how do SQL developer get into their house?\nWith keys"
        if ranNum == 14:
            text = "What is a programmers favorite exercise activity?\nSprint"
        if ranNum == 15:
            text = "Why do IT people wear glasses\nBecause they don't C#"
        if ranNum == 16:
            text = "why was there no windows 9? \nbecause windows 7 8 9."
        if ranNum == 17:
            text = "What did the fish say when he sawm into a wall?\nDam."
        if ranNum == 18:
            text = "What is a computer???s favorite snack?\nComputer chips"
        if ranNum == 19:
            text = "What did the ocean say to the boat?\nNothing it just wave"
        if ranNum == 20:
            text = "What type of aniaml will always be in your computer?\n RAM"
        if ranNum == 21:
            text = "What animal is always at a baseball game?\nA bat."
        if ranNum == 22:
            text = "What did the little corn say to the mama corn?\nWhere is pop corn?"
        if ranNum == 23:
            text = "What kind of tree fits in your hand?\nA Palm Tree"
        if ranNum == 24:
            text = "Why did the teddy bear say no to dessert?\nBecause she was stuffed."
        if ranNum == 25:
            text = "What did one plate say to the other plate?\nDinner is on me."
        if ranNum == 26:
            text = "Why did the student eat his homework?\nBecause the teacher told him it was a piece of cake."
        if ranNum == 27:
            text = "What did the tiger say to her cub on his birthday?\nIt???s roar birthday."
        if ranNum == 28:
            text = "Why was the equal sign so humble? \nBecause he wasn???t greater than or less than anyone else."
        if ranNum == 29:
            text = "How do you stay warm in any room? \nAt the cornor because it's always 90 degrees."
        if ranNum == 30:
            text = "Why does nobody talk to circles?\nBecause there???s no point."
        return text
