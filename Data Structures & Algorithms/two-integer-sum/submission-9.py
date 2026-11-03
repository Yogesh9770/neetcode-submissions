class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i , num in enumerate(nums):
            total = target-num
            if total in seen:
                return [seen[total],i]
            seen[num]=i
        return []
