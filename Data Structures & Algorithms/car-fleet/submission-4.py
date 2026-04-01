class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [] # [pos, speed]
        for pos, speed in zip(position, speed):
            cars.append([pos, speed])
        cars.sort(reverse=True)

        stack = []

        for i in range(0, len(cars)):
            pos, speed = cars[i]
            time = (target - pos) / speed
            stack.append(time)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)




        


        