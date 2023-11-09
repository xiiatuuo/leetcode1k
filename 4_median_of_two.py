class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
      
        def get_k(k):
            idx1, idx2 = 0, 0
           
            while True:
                if idx1 == m:
                    return nums2[idx2 + k - 1]
                if idx2 == n:
                    return nums1[idx1 + k - 1]
                if k == 1:
                    return min(nums1[idx1], nums2[idx2])

                # 正常情况
                n_idx1 = min(idx1 + k // 2 - 1, m - 1)
                n_idx2 = min(idx2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[n_idx1], nums2[n_idx2]
                if pivot1 <= pivot2:
                    k -= n_idx1 - idx1 + 1
                    idx1 = n_idx1 + 1
                else:
                    k -= n_idx2 - idx2 + 1
                    idx2 = n_idx2 + 1

        m = len(nums1)
        n = len(nums2)
        if (m + n)  % 2 == 0:
            return (get_k((m+n)//2) +  get_k( (m+n)//2+1) ) /2.0
        else:
            return get_k((m+n+1)//2)

