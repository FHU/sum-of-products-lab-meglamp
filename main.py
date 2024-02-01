#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks
def sum_of_products(list1, list2):
    lst1 = []
    lst2 = []
    num = 0
    for letter in list1:
        lst1.append(letter)
    for letter in list2:
        lst2.append(letter)

    for i in range(0,len(list1)):
        num = num + (int(lst1[i])*int(lst2[i]))
    return(num)
        

lis1 = input()
lis2 = input()
if len(lis1) == len(lis2):
    number = sum_of_products(lis1,lis2)
    print(number)
else:
    print("error")
    

