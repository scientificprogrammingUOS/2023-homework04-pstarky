import numpy as np 

# implement your function to combine two numpy arrays 

def combination(arrayOne, arrayTwo, axis=0):
    '''Write a function combination that takes in two numpy arrays and an optional parameter axis which should be 0 by default. 
    Remove unnecessary dimensions of the input arrays, 
    check whether they can be combined along the given axis and return the combined array. 
    If the combination is not possible, raise a meaningful error message.'''
    
    # Remove unnecessary dimensions of the input arrays, 
    arrayOne = arrayOne.squeeze()
    arrayTwo = arrayTwo.squeeze()

    print(arrayOne.shape)
    print(arrayTwo.shape)
    print(arrayOne)
    print(arrayTwo)

    try:
        combination = np.concatenate((arrayOne, arrayTwo) , axis)
        return combination 
    except:
        print('The two arrays can not be combined.')
        


if __name__ == "__main__":
    # use this for your own testing!
    arrayONE = np.array([4,5,6,7,8,9,0])
    arrayTWO = np.array([4,5,6,7,8,9,0])

    print(combination(arrayONE, arrayTWO, 0))

    a = np.array([[[[1, 2], [3, 4], [5, 6]]]])
    b = np.ones((2,2))
    

    print(combination(a, b))

    pass

