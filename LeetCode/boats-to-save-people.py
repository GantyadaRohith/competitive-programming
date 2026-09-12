class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        cnt = 0
        high = len(people)-1
        for i in range(len(people)-1,-1,-1):
            if people[i]>=limit:
                cnt+=1
            else:
                high = i
                break
        low = 0
        while low <= high:
            if people[low]+people[high] <= limit:
                cnt+=1
                low+=1
                high-=1
            else:
                cnt+=1
                high-=1
        return cnt