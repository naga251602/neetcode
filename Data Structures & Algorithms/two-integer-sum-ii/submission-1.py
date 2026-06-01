class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        st, en = 0, len(numbers) - 1

        while st < en:
            t = numbers[st] + numbers[en]
            if t == target: return [st+1, en+1]
            elif t < target: st += 1
            else: en -= 1
        
        return []