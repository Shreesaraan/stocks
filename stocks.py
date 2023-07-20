def stocks(array):
    min=float('inf')
    max=float('-inf')
    for i in range(len(array)):
        if array[i]<min:
            min=array[i]
    for i in range(min,len(array)):
        if array[i]>max:
            max=array[i]
    return max-min

array=list(map(int,input("Enter the Array Elements : ").split()))
print(stocks(array))