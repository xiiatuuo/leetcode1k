class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            if i>=1 and nums[i] == nums[i-1]:
                continue
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    right -= 1
                    # print("s = 0 , i=%d|left=%d|right=%d" %(i, left, right))
                elif s > 0:
                    ''' 这段注释与否都能通过'''
                    # while left < right and nums[right] == nums[right-1]:
                    #     right -= 1
                    right -= 1
                    # print("s > 0 , i=%d|left=%d|right=%d" %(i, left, right))
                else:
                    ''' 这段注释与否都能通过'''
                    # while left < right and nums[left] == nums[left+1]:
                    #     left += 1
                    left += 1
                    # print("s < 0 , i=%d|left=%d|right=%d" %(i, left, right))
                    
        return ans
