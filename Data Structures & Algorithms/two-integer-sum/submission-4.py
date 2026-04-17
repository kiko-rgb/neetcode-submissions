class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {}
        for i in range(len(nums)):
            delta = target - nums[i]
            if delta in diff_map.keys():
                return [diff_map[delta], i]
            else:
                diff_map[nums[i]] = i     
        