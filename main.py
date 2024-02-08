#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks
def sum_of_products(list1, list2):
    num = 0

    for i in range(0,len(list1)):
        par1 = int(list1[i])
        par2 = int(list2[i])
        num = num + (par1*par2)
    return(num)



if __name__ == '__main__':
    list1 = input()
    list2 = input()
    list1 = list1.split()
    list2 = list2.split()
    number = sum_of_products(list1,list2)
    print(number)
    


