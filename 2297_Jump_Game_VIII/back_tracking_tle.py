class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        def first_con(l, r):
            for i in range(l + 1, r):
                if nums[i] >= nums[l]:
                    return False
            return True

        def second_con(l, r):
            for i in range(l + 1, r):
                if nums[i] < nums[l]:
                    return False
            return True

        def helper(idx, cost):
            if cost >= self.res:
                return
            if idx == len(nums) - 1:
                self.res = min(self.res, cost)
            for i in range(idx + 1, len(nums)):
                if nums[idx] <= nums[i] and first_con(idx, i):
                    helper(i, cost + costs[i])
                elif nums[idx] > nums[i] and second_con(idx, i):
                    helper(i, cost + costs[i])

        self.res = math.inf
        helper(0, 0)
        return self.res