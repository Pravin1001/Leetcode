class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ls=0
        rs=sum(nums)  
        for i,e in enumerate(nums):
            rs-=e
            if ls==rs:
                return i
            ls+=e
        return -1
