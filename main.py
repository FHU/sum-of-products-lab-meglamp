#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks
def sum_of_products(list1, list2):
    total = 0
    li1 = int(list1)
    li2 = int(list2)

    for i in range(0,len(list1)):
        if i == 0:
            listy1 = li1 % 10
            listy2 = li2 % 10 
        else:
            li1 = li1 // 10
            li2 = li2 //10
            listy1 = li1 % 10
            listy2 = li2 % 10
        numby = listy1 * listy2
        total = total + numby
    return(total)
        

if __name__ == '__main__':
    lis1 = input()
    lis2 = input()
    if lis1.isdigit():
        if len(lis1) == len(lis2):
            number = sum_of_products(lis1,lis2)
            print(number)
        else:
            print("error")
    else:
        print("error")
    

