from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)
        for n in num_set :
            if n - 1 not in num_set :
                length = 1
                while n + length in num_set :
                    length +=1 
                longest = max(longest, length)
        return longest
    
if __name__ == "__main__" :
    nums = [0,3,7,2,5,8,4,6,0,1]
    algo = Solution()
    longest_cons_set = algo.longestConsecutive(nums)
    print(longest_cons_set)
                