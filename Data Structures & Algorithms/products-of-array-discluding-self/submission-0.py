class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            mult_list = nums.copy()
            result = 1
            for j in range(len(mult_list)):
                if j != i:
                    result *= mult_list[j]
            res.append(result)
        return res