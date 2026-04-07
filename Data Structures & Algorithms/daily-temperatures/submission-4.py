class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        length = len(temperatures) - 1
        count = 0
        for i in range(len(temperatures)):
            current_day = temperatures[i]
            print(current_day)
            if i == length:
                result.append(0)
                count = 0
            for j in range(i + 1 ,len(temperatures)):
                count+=1
                print(j)
                if current_day < temperatures[j]:
                    result.append(count)
                    count = 0
                    break
                elif j == length:
                    result.append(0)
                    count = 0
        return result


