arr= [1,2,3,4,5,6,7,8,9,10]

def calculate_mean(arr):
    return sum(arr)/len(arr)

mean= calculate_mean(arr)
print("Mean =" ,mean)

arr2= [1, 2, 3, 7]
arr2median= (arr2[len(arr2)]//2 - 1) + (arr2[len(arr2)]//2)

arr3= [1, 9, 4]
arr3median= (arr3[len(arr3)//2])

def calculate_median_even(arr2):
        print("Median of even length of numbers=" ,arr2median)
        
def calculate_median_odd(arr2):
    print("Median of odd length of numbers=" ,arr3median)