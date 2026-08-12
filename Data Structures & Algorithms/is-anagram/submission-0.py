class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp_s = sorted(s)
        temp_t = sorted(t)
        return temp_s == temp_t