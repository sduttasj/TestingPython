class Solution:
    def letterCasePermutation(self, s: str):
        def compute(ip, op):
            if len(ip) == 0:
                out.append(op)
                return
            op1 = op
            if not ip[0].isdigit():
                if ip[0].islower():
                    compute(ip[1:], op1 + ip[0].upper())
                else:
                    compute(ip[1:], op1 + ip[0].lower())
            compute(ip[1:], op1 + ip[0])
            return
        ip = s
        op = ""
        out = []
        compute(ip, op)
        
        return out