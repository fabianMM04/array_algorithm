
def canBeSplitted(arr) :
    """
    Function that split the array in equal sum and return:
    * 1 if can be splitted
    * 0 if array is empty
    * -1 if can't be splitted
    """
    n = len(arr)

    if (n > 0):

        leftSum = 0
        for i in range(0, n) :
            # total sum left
            leftSum += arr[i]
    
    
        rightSum = 0
        for i in range(n-1, -1, -1) :
    		# total sum rigth
            rightSum += arr[i]
    
    		
            leftSum -= arr[i]
    		# Compare if sum left and rigth are equal
            if (rightSum == leftSum) :
                return 1
    else:
        return 0
            
    return -1

if __name__ == '__main__':
    arr = [1 , 3 , 3 , 8 , 4 , 3 , 2 , 3 , 3]
    print(canBeSplitted(arr))
