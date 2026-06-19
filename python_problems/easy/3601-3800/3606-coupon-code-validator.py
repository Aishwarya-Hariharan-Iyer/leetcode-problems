import re

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        pattern = re.compile(r"^[A-Za-z0-9_]+$")
        coupons = zip(code, businessLine, isActive)
        validCoupons = list(filter(
            lambda x: x[2]
            and (x[1] in ["electronics", "grocery", "pharmacy", "restaurant"])
            and (pattern.match(x[0]) != None)
            , coupons))
        validCoupons.sort(key=lambda x: (x[1], x[0]))
        return list(map(lambda x: x[0], validCoupons))
        
        
