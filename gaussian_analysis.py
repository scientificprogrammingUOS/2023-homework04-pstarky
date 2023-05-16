import numpy as np


# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):
    
    # check formats of the variables
    if type(loc) != (int or float):
        # print(TypeError('At least one of the variables is not in the right format. Please, make sure to use ONLY integers or floats'))
        return TypeError('At least one of the variables is not in the right format. Please, make sure to use ONLY integers or floats')
    elif type(scale) != (int or float) :
        # print(TypeError('At least one of the variables is not in the right format. Please, make sure to use ONLY integers or floats'))
        return TypeError('At least one of the variables is not in the right format. Please, make sure to use ONLY integers or floats')
    elif type(lower_bound) != (int or float):
        # print(TypeError('At least one of the variables is not in the right format. Please, make sure to use ONLY integers or floats'))
        return TypeError('At least one of the variables is not in the right format. Please, make sure to use ONLY integers or floats')
    elif type(upper_bound) != (int or float):
        # print(TypeError('At least one of the variables is not in the right format. Please, make sure to use ONLY integers or floats'))
        return TypeError('At least one of the variables is not in the right format. Please, make sure to use ONLY integers or floats')
    
    # check boundaries
    elif upper_bound <= lower_bound:
        # print(TypeError('lower_bound is not smaller than upper_bound')) 
        return TypeError('lower_bound is not smaller than upper_bound')

    gaussian =  np.random.normal(loc, scale, 100)
    # print(gaussian)

    # filtering with masks
    maskL = lower_bound <= gaussian
    # print(maskL)
   
    gaussian = gaussian[maskL]
    # print(gaussian) 

    maskU = gaussian <= upper_bound

    gaussian = gaussian[maskU]
    # print(gaussian)

    # mean = np.sum(gaussian)/len(gaussian)
    # print(mean == np.mean(gaussian))
    mean = np.mean(gaussian)
    std = np.std(gaussian)

    return (mean, std)

if __name__ == "__main__":
    # use this for your own testing!
    print(gaussian_analysis(4,4,4,6))
    pass

