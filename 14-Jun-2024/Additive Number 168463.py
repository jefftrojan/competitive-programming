# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        def valid(s):
            if s == "0":
                return True
            if s.startswith("0"):
                return False
            return True
        
        def add_num(prev_1, prev_2, indx, flag):
            if indx == len(num) and flag:
                return True
            for i in range(indx, len(num)):
                sub_str = num[indx: i+1]
                if valid(sub_str):
                    if prev_1 == None:
                        if add_num(int(sub_str), prev_2, i+1, False):
                            return True
                    else:
                        if prev_2 == None:
                            if add_num(prev_1, int(sub_str), i+1, False):
                                return True
                        else:
                            if int(sub_str) == prev_1 + prev_2:
                                if add_num(prev_2, int(sub_str), i+1, True):
                                    return True
            return False
        return add_num(None, None, 0, False)



            





                
                