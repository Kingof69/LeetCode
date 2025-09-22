from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        merged = list(zip(position, speed))

        merged.sort(key=lambda x: x[0], reverse=True)

        times = [(target - p) / s for p, s in merged]

        s = [times[0]]
        m = times[0]

        for i in times:
            if i > m:
                s.append(i)
                m = i
            
        return len(s)

# Example usage:
solution = Solution()
print(solution.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))  # Output: 3
print(solution.carFleet(10, [3], [3]))                    # Output: 1