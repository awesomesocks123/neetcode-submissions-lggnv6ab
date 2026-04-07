class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            #lets check if we can eat all banana's in every pile with this speed
            #k represeent the speed
            total_time = 0 
            for pile in piles:
                time = pile // k # this is how long it takes to eat this current pile
                if pile % k > 0: # check for remainder so we know to add an additional hour
                    time += 1
                total_time += time # this to gatehr how many time it takes in total
            return total_time <= h # we know to decrement right here 




        left, right = 1, max(piles) # fastest we can eat is the largest pile in the pile in one hour
        while left <= right:
            mid = left + (right - left) // 2

            if check(mid):
                res = mid #store our potential answer
                right = mid - 1
            else:
                left = mid + 1

        return res