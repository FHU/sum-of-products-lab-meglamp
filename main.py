#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks
def sum_of_products(list1, list2):
    num = 0

    for i in range(0,len(list1)):
        num = num + (int(list1[i])*int(list2[i]))
    return(num)
        

if __name__ == '__main__':
    lis1 = input()
    lis2 = input()
    if len(lis1) == len(lis2):
        number = sum_of_products(lis1,lis2)
        print(number)
    else:
        print("Error: numbers must be the same length")

