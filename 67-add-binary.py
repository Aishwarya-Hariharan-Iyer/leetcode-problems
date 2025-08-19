class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = "0" + a
        b = "0" + b

        la = len(a)
        lb = len(b)
        diff = abs(la-lb)
        to_buff = "0"*diff

        if la < lb:
            a = to_buff + a
        if lb < la:
            b = to_buff + b

        la = len(a)
        lb = len(b)
        pa = la-1
        pb = lb-1

        #res = ""
        res = ["0"]*la
        carry_over = False

        while pa > -1 and pb > -1:
            if a[pa] == "0" and b[pb] == "0":
                #res = "0" + res if not carry_over else "1" + res
                res[pa] = "0" if not carry_over else "1"
                carry_over = False if carry_over else carry_over
                pa-=1
                pb-=1
            elif a[pa] == "1" and b[pb] == "1":
                #res = "1" + res if carry_over else "0" + res
                res[pa] = "1" if carry_over else "0"
                carry_over = True 
                pa-=1
                pb-=1
            else:
                #res = "0" + res if carry_over else "1" + res
                res[pa] = "0" if carry_over else "1"
                carry_over = True if carry_over else carry_over
                pa-=1
                pb-=1
        
        if res[0] == "0":
            res = res[1:]

        return ("").join(res)
