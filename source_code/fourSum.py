def fourSum(nums,target):
    ans=list()
    n=len(nums)
    if n<4:
        return ans
    nums.sort()
    for f in range(n):
        if f and nums[f]==nums[f-1]:
            continue
        for s in range(f+1,n):
            if s>f+1 and nums[s]==nums[s-1]:
                continue
            fo=n-1
            for t in range(s+1,n):
                if t>s+1 and nums[t]=nums[t-1]:
                    continue
                while t<fo and nums[f]+nums[s]+nums[t]+nums[fo]>target:
                    fo -=1
                if t==fo:
                    break
                if nums[f]+nums[s]+nums[t]+nums[fo]==target:
                    ans.append([nums[f],nums[s],nums[t],nums[fo]])
    return ans
