def permutation(array, index, size):
    if index==size:
        print(array)
    else:
        for i in range(index,size):
            array[i],array[index]=array[index],array[i]
            permutation(array,index+1,size)
            array[i],array[index]=array[index],array[i]
array=[1,2,3]
size=len(array)
permutation(array,0,size)