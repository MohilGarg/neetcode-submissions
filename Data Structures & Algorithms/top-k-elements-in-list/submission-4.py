class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        buckets = [[] for i in range(len(nums) + 1)]

        for num, count in hashmap.items():
            buckets[count].append(num)

        res = []

        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
