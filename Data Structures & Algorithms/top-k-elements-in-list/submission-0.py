class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = dict()
        for num in nums:
            res[num] = res.get(num, 0) + 1
        
        reverse_sorted_nums = sorted(res.items(), key=lambda item: item[1], reverse=True)

        ans = []
        for i in range(k):
            ans.append(reverse_sorted_nums[i][0])

        return ans