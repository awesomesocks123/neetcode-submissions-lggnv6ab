class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        n cars traveling 

        position[i] is the position of the ith car

        speed[i]  is the speed of the ith car

        destination is the position target miles

        car can't pass another car ahead of it 
        - can only catch up to another car then drive at the same speed as the car ahead


        a car fleet is a non-empty set of cars driivng at the same position and same speed
        single car can also be considered a car fleet


        if car catches up to a car fleet the moment hte fleet reaches the destination the car is 
        part of the fleet

        return the number of different car fleets that will arrive at the destination





        
        
        
        """

        # put the speed and position as pairs
        pair = [(p,s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        # setting up from reverse so we know from least to greatest we only need to pop if we have dupes
        stack = []

        for p, s in pair:
            stack.append((target - p)/ s) # distance formula  (target - position) / speed 
            if len(stack) >= 2 and stack[-1] <= stack[-2]: #check for dupes
                stack.pop()
        return len(stack)

