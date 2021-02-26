def merge(from_a,to_a,low,mid,high):
    i,j,k=low,mid,low
    while i<mid and j<high:
        if from_a[i]<=from_a[j]:
            to_a[k]=from_a[i]
            i+=1
        else:
            to_a[k]=from_a[j]
            j+=1
        k+=1
    while i<mid:
        to_a[k]=from_a[i]
        i+=1
        k+=1
    while j<high:
        to_a[k]=from_a[j]
        j+=1
        k+=1
def merge_pass(from_a, to_a, length, seg_len):
    i=0
    while i+2*seg_len<length:
        merge(from_a, to_a, i, i+seg_len, i+2*seg_len)
        i+=2*seg_len
    if i+seg_len<length:
        merge(from_a, to_a, i, i+seg_len, length)
    else:
        to_a[i:]=from_a[i:]

def merge_sort(array,target):
    flag=0
    seg_len, length=1, len(array)
    temp_list=[None]*length
    while seg_len<length:
        merge_pass(array, temp_list, length, seg_len)
        seg_len *=2
        if temp_list==target:
            flag=2
        if flag=3:
            print_list(array,flag)
            break
        merge_pass(temp_list,array, length, seg_len)
        seg_len *=2
        if array==target:
            flag=3
        if flag==2:
            print_list(array,flag)
            break
array=list(map(int,input().split()))
print(array)
merge_sort(array)
