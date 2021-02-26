def findMedianSortedArrays(nums1,nums2):
    length1=len(nums1)
    length2=len(nums2)
    length=(length1+length2)-1
    ans=[]
    i=0
    k=0
    while i<length1 and k<length2:
        if nums1[i]<= nums2[k]:
            ans.append(nums1[i])
            i+=1
        else:
            ans.append(nums2[k])
            k+=1
    while i<length1:
        ans.append(nums1[i])        
        i+=1
            
    while k<length2:
        ans.append(nums2[k])         
        k+=1
        
    print(ans,length)
    if length%2==0:
        return ans[length//2]
    else:
        return (ans[length//2]+ans[length//2+1])/2
nums1 = []
nums2 = [1,1,3,]
print(findMedianSortedArrays(nums1,nums2))