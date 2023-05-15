import math

#Initial solution 
# multiple all values in array 
# for i in the range of the size of the array, divide the total product by the value at i 
# set the value at i to the current total 

# def productWithoutCurrentValue(arr):
#     total_product = math.prod(arr)
#     result = []

#     for i in range(len(arr)):
#         result.append(int(total_product / arr[i]))


#     return result

# print(productWithoutCurrentValue([1, 2, 3, 4, 5]))

# Follow up question - solve without division 

def productWithoutCurrentValue(arr):
    result = [1] * len(arr)

    for i in range(len(arr)):
        for j in range(len(arr)):
            if j != i:
                result[j] = arr[i] * result[j]
                
    return result
    

    

print(productWithoutCurrentValue([1, 2, 3, 4, 5]))


    


