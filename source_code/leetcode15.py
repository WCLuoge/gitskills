def threeSum(nums):
    n=len(nums)
    ans=list()
    nums.sort()

    if n<3:
        return ans

    for first in range(n):
        if first and nums[first]==nums[first-1]:
            continue
        third=n-1
        target=-nums[first]

        for second in range(first+1,n):
            if second>first+1 and nums[second]==nums[second-1]:
                continue
            while second<third and nums[second]+nums[third]>target:
                third -=1
            if second==third:
                break
            if nums[second]+nums[third]==target:
                ans.append([nums[first], nums[second], nums[third]])
    return ans
nums=[0,2,1,-3]
print(threeSum(nums))