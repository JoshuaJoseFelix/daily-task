class Solution:
    def reverse(self, x: int) -> int:
   
        # Determine the sign
        sign = -1 if x < 0 else 1

        # Work with the absolute value as a string
        x_str = str(abs(x))
        
        # Reverse using string slicing (cleaner than a for loop)
        reversed_str = x_str[::-1]
        
        # Convert back to integer with the correct sign
        result = sign * int(reversed_str)
        
        # 32-bit overflow check
        if result < -2**31 or result > 2**31 - 1:
            return 0
            
        return result
