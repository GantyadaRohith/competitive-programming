class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        hr1,min1,sec1 = int(startTime[0:2]),int(startTime[3:5]),int(startTime[6:])
        hr2,min2,sec2 = int(endTime[0:2]),int(endTime[3:5]),int(endTime[6:])
        st = hr1*3600 + min1 * 60 + sec1
        et = hr2*3600 + min2 * 60 + sec2
        print(hr2,min2,sec2)
        return et-st
        