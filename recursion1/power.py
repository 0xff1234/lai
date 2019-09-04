
class Solution(object):
    def apowb(self, a, b):
        if a == 0 or b == 0:
            return 1
        # if b == 1:
        #     return a

        midB = int(b /2)
        halfResult = self.apowb(a, midB)

        modB = b % 2
        if modB == 0:
            return halfResult * halfResult
        else:
            return halfResult * halfResult * a

so = Solution()
print(so.apowb(2, 11))