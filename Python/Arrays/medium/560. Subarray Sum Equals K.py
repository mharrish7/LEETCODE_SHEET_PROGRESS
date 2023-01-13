class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            if nums[0] == k:
                return 1 
            else:
                return 0
        prefix = [0]*len(nums)
        prefix[0] = nums[0]

        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] + nums[i]
        
        ans = 0 
        
        hast = {}
        for i in prefix:
            if i == k:
                ans +=1 
            if i-k in hast:
                ans += hast[i-k]
            if i in hast:
                hast[i]+=1 
            else:
                hast[i] = 1

        return ans