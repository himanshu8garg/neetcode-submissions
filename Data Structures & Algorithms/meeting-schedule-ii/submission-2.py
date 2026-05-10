"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_time, end_time = [], []
        for interval in intervals:
            start_time.append(interval.start)
            end_time.append(interval.end)
        
        start_time=sorted(start_time)
        end_time = sorted(end_time)
         
        #Now we have the sorted time 
        start,end = 0,0
        curr_room = 0
        result = 0
        while start<len(start_time):
            if start_time[start] < end_time[end]:
                ##room is occupied
                start+=1
                curr_room +=1

            else:
                end+=1
                curr_room-=1
            result = max(curr_room, result)
        return result
