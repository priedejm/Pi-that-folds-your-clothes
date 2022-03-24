# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re
import array

with open ("dataSheet.txt", "r") as file:
    #dataNum =[0,0,0,0,0,0,0,0]
    dataNum = array.array('i',[0,0,0,0,0,0,0,0])
    count = 0
    for line in file:    
        anum = int(re.search(r'\d+', line).group())
        dataNum.insert(count,anum)
        #print(anum)
        count += 1
    for i in range (0, 8):
        print (dataNum[i], end = " ")
    print()
    file.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
