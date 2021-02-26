def threeSumClosest(nums,target):
    def close_abs(f,s,t):
        return abs(nums[f]+nums[s]+nums[t]-target)
    n=len(nums)
    nums.sort()
    close=close_abs(-1,-2,-3)
    ans=nums[-1]+nums[-2]+nums[-3]
    for f in range(n):
        if f and nums[f]==nums[f-1]:
            continue

        for s in range(f+1,n):
            if s > f+1 and nums[s]==nums[s-1]:
                continue
            for t in range(s+1,n):
                if t> s+1 and nums[t]==nums[t-1]:
                    continue
                new=close_abs(f,s,t)
                if new==0:
                    return nums[f]+nums[s]+nums[t]
                if new<close:
                    ans=nums[f]+nums[s]+nums[t]
                    close=new
                    
                    
    return ans
nums=[1,1,-1,-1,3]
target=1
print(threeSumClosest(nums,target))
