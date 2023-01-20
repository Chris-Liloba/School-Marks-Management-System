#A program that gives you a list of marks  by asking the user to fill the marks and then getting total and the mean

myList = [] #marks


kiswahili, maths, english, history, GHCRE= int(input("KISWAHILI: ")), int(input("MATHS: ")), int(input("ENGLISH: ")), int(input("HISTORY: ")), int(input("GHCRE: "))

myList.append(kiswahili)
myList.append(maths)
myList.append(english)
myList.append(history)
myList.append(GHCRE)



print(f"+++++++-----MARKS OF CLASS 8 RED+++++++-----:\n {myList}")

totalMarks = kiswahili + maths + english + history + GHCRE
print(f"+++++++-----TOTAL MARKS+++++++-----:\n {totalMarks}")


for list_1 in myList:
    list_1 += list_1
    print(f" list_1: {list_1}")
MeanGrade = (kiswahili + maths + english + history + GHCRE)/5
print(f"+++++++-----MeanGrade+++++++-----:\n {MeanGrade}")