class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        if len(intervals) == 1:
            return intervals
        new_intervals = []
        start = intervals[0][0]
        end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            if end >= intervals[i][0]:
                end = max(end, intervals[i][1])
                start = min(intervals[i][0], start)
            else:
                new_intervals.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
        
            if i == len(intervals) - 1:
                    new_intervals.append([start,end])
                    
        return new_intervals