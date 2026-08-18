class Solution:

    def find_index(self, nums: List[int], comp: int) -> int:
        for i in range(len(nums)):
            if nums[i] == comp:
                return i

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = set()
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in s:
                return [self.find_index(nums, comp), i]
            else:
                s.add(nums[i])