class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1 = len(num1)
        l2 = len(num2)
        ans = ["0"] * (max(l1, l2) + 1)

        #right align numbers
        p1 = l1-1
        p2 = l2-1
        p3 = len(ans) - 1
        carry = 0

        while p1 >= 0 and p2 >= 0:
            s = int(num1[p1]) + int(num2[p2]) + carry
            digit = s % 10
            carry = s // 10
            ans[p3] = str(digit)
            p1 -= 1
            p2 -= 1
            p3 -= 1
        
        while p1 >= 0:
            s = int(num1[p1]) + carry
            digit = s % 10
            carry = s // 10
            ans[p3] = str(digit)
            p1 -= 1
            p3 -= 1

        while p2 >= 0:
            s = int(num2[p2]) + carry
            digit = s % 10
            carry = s // 10
            ans[p3] = str(digit)
            p2 -= 1
            p3 -= 1

        ans[p3] = str(carry)

        ans = ''.join(ans)
        return ans.lstrip('0') if float(ans) != 0 else "0"
            
