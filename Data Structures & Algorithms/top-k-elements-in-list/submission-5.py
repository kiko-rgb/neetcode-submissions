class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        sorted_ids = sorted(freq.values())
        print(sorted_ids)
        return sorted(freq.keys(), key=lambda x: freq[x])[-k:]