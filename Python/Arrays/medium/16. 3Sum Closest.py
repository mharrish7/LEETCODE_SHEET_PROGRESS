
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        difres = float('inf')
        res = 0
        nums.sort()
        for i in range(len(nums)):
            l,r = i+1,len(nums) - 1
            while l<r:
                sumn = nums[i] + nums[l] + nums[r]
                if sumn > target:
                    r-=1
                elif sumn < target:
                    l+=1
                else:
                    return sumn 
                if difres > abs(target-sumn):
                    difres = abs(target - sumn)
                    res = sumn
        return res
        