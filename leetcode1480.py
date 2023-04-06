class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res=[]
        temp=[]
        for i in range(len(nums)):
            temp.append(nums[i])
            res.append(sum(temp))
        return res
