class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {}
        for i in range(len(nums)):
            print(target, nums[i])
            delta = target - nums[i]
            print(delta)
            if delta in diff_map.keys():
                return [diff_map[delta], i]
            else:
                diff_map[nums[i]] = i     
                print(diff_map)       
        