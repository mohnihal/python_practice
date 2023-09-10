'''evaluate prefix equation'''

import operator

class Solution:
    def __init__(self):
        self.operator_mapping = {"+":operator.add,
                            "-":operator.sub,
                            "/":operator.floordiv,
                            "*":operator.mul,
                                }


    def compute(self,operand1,operand2,operator_symbol):
        # print (operand1,operand2,operator_symbol)
        # print (int(self.variables.get(operand2,operand2)))
        return self.operator_mapping[operator_symbol](int(self.variables.get(operand1,operand1)),int(self.variables.get(operand2,operand2)))
        pass

    def evaluatePrefix(self,expression,variables={}):
        stack=[]
        self.variables=variables
        expression = list(expression)
        while(expression):
            val=expression.pop()
            
            if val in self.operator_mapping:
                op1=stack.pop()
                op2=stack.pop()
                stack.append(self.compute(op1,op2,val))
            else:
                stack.append(val)
        
        return stack.pop()

sol=Solution()
# print(sol.evaluatePrefix("+6*-4+2x8",{"x":3}))
# print(sol.evaluatePrefix("-+7*45+20",{"x":3}))
print(sol.evaluatePrefix("* + 1 2 3 ",{"x":3}))