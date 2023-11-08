class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not len(nums):
            return -1
        st = 0
        et = len(nums) - 1
        while et >= st:
            mid = (st + et) / 2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                st = mid + 1 
            if target < nums[mid]:
                et = mid - 1
        return -1
