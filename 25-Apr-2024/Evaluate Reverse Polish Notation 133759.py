# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        for i in tokens:
            if i.isnumeric() or (i[0] == '-' and i[1:].isnumeric()):
                s.append(int(i))
            elif i in ['+','-','*','/']:
                op2=s.pop()
                op1=s.pop()
                if i == '+':
                    res=op1+op2
                elif i == '-':
                    res=op1-op2
                elif i == '*':
                    res=op1*op2
                else:
                    res= int(op1 / op2)
                s.append(res)
        return s.pop()
            
        