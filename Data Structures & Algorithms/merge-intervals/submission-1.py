class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda t:(t[0], t[1]))
        output = [sorted_intervals[0]]

        for start, end in sorted_intervals[1:]:
            if start <= output[-1][1]:
                output[-1][1] = max(end, output[-1][1])
            else:
                output.append([start, end])
        return output