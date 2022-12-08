class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = {}
        for x in nums:
            dict[x] = dict.get(x,0) + 1

        for k, v in dict.items() :
            if v == 0