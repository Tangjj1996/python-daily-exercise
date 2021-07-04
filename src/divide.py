class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        flag = -1 if (dividend > 0 and divisor <
                      0) or (dividend < 0 and divisor > 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        p, times = 0, 0

        while(dividend >= divisor):
            cur = dividend - (divisor << times)

            if cur >= 0:
                p += (1 << times)
                times += 1
                dividend = cur
            else:
                times -= 1
        return max(-2 ** 31, min(p * flag, 2 ** 31 - 1))


dividend, divisor = -2147483648, 1
print(Solution.divide(Solution, dividend, divisor))
