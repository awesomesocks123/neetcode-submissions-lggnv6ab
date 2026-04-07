class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # we first get the time
        # time = target - position[i] // speed[i]
        # we then pick out cars with the same time
        # if they're the same time they're part of one fleet
        # separate by different fleets

        # we can use a dictionary to count the diff fleets 
        # our key  is time and value is count
        cars = []
        arrival_times = []
        for i in range(len(position)):
            cars.append((position[i],speed[i]))
        cars.sort()
        cars.reverse()
        for c in cars:
            pos, speed = c[0],c[1]
            print(pos,speed)
            arrival_times.append((target-pos)/speed)
        stack = [arrival_times[0]]
        for c in arrival_times:
            if c <= stack[-1]:
                continue
            else:
                stack.append(c)

        return len(stack)