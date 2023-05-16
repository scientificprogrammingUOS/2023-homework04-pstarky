import numpy as np

# implement the function strange pattern
'''Mesmerized, you decide you must write a function to generate arbitrary sizes of it. 
(Write a function strange_pattern that takes a shape tuple (n, m) as input and generates a boolean 
(True for x's and False for blank spaces) 2D NumPy array of the given shape with this pattern)

Hint: Perhaps this strange symbol might help? ::
'''

def strange_pattern(tuple):
    # get m and n
    n = tuple[0]
    m = tuple[1]
    # number of elements
    elements = n*m
    # print(elements)
    # arrange output array
    output = np.arange(elements).reshape((n, m))
    #  print(output, '/n')

    for i in range(n):
        # print(output[i,-i%3:elements:3])
        # assign truth values
        output[i,(-i+3)%3:elements:3] = True
        output[i,(-i+1)%3:elements:3] = False
        output[i,(-i+2)%3:elements:3] = False
    print(output)
    # cast into boolean valurs
    output = output ==  1
    # return the reulting array
    return(output)


if __name__ == "__main__":
    # use this for your own testing!
    print(strange_pattern(( 2, 2)))
    pass

print(type(tuple([6,56])))
print()