class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        left = 0
        right = len(nums) -1
        while left <right:
            total = nums[left] + nums[right]
            if total==target:
                return [left,right]
            elif total<target:
                left = left+1
            else:
                right = right-1