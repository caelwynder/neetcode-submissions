class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h = defaultdict(int)

        maxcount = 0

        for n in nums:
            h[n] += 1
            if maxcount < h[n]:
                res = n
                maxcount = h[n]

        return res
