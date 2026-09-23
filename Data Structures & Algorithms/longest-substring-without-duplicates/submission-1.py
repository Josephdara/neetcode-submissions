class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        maxLength = 0
        solution_set = set()
        for right in range(len(s)):
            while s[right] in solution_set:
                solution_set.remove(s[left])
                left += 1
            solution_set.add(s[right])
            maxLength = max(len(solution_set), maxLength)
        return maxLength



        