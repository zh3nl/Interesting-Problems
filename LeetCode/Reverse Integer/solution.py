class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0
        original = x

        if x < 0:
            x = x * -1

        while x > 0:
            reverse = reverse * 10 + x % 10
            x = x // 10
        
        if reverse < -2 ** 31 or reverse > 2 ** 31 - 1:
            return 0
        elif original < 0:
            return reverse * -1
        else: 
            return reverse
        
