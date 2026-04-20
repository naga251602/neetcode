class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        count = 0
        l, r = 0, len(people) - 1

        while l <= r:
            print(people[l], people[r])
            if people[l] + people[r] <= limit: 
                l += 1
                r -= 1
            elif people[r] <= limit:
                r -= 1
            else:
                l += 1
            
            count += 1

        return count
