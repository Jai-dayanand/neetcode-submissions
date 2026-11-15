
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            ind1 = i
            diff = target - nums[i]

            if diff in nums:
                ind2 = nums.index(diff)

                if ind1 != ind2:
                    return sorted([ind1, ind2])

        return 
