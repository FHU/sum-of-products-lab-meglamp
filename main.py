#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks
def sum_of_products(list1, list2):
    num = 0

    for i in range(0,len(list1)):
        par1 = int(lis1[i])
        par2 = int(lis2[i])
        num = num + (par1*par2)
    return(num)
        

if __name__ == '__main__':
    lis1 = input()
    lis2 = input()
    number = sum_of_products(lis1,lis2)
    print(number)
    

