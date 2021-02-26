def combination(n,m,array1,array2):
    for i in range(n,m-1,-1):
        array2[m-1]=i-1
        if m>1:
            combination(i-1,m-1,array1,array2)
        else:
            print([array1[i] for i in array2[::-1]])
array1=[1,2,3,4,5]
m=3
array2=[0]*m
n=len(array1)
combination(n,m,array1,array2)