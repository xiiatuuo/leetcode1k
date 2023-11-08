class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not len(intervals):
            return []
        intervals.sort(key=lambda d:d[0])
        print(intervals)
        result_list = []
        start = intervals[0][0]
        end = intervals[0][1]
        for v in intervals[1:]:
            if v[0] > end:
                result_list.append([start, end])
                start = v[0]
                end = v[1]
            else:
                if v[1] > end:
                    end = v[1]
        result_list.append([start, end])
        return result_list
