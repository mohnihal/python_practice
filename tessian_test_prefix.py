#!/bin/python3
import os
import sys



# from typing import Dict, Optional, Tuple
import operator

operator_mapping = {"+":operator.add,
                    "-":operator.sub,
                    "*":operator.mul,
                    "/":operator.floordiv
                    }

# Complete the max_result_expression function below.
# You may add any imports you require from the standard library.
# Feel free to define your own helper functions, classes etc as you see fit.


def compute(operand1,operand2,operator_symbol,_variables):
    print (operand1,operand2,operator_symbol,_variables)
    result_list = []
    if operand1.isdigit() or operand1.lstrip("-").isdigit():
        operand1 = (int(operand1),int(operand1)+1)
    else:
        operand1 = _variables.get(operand1,None)
    if operand2.isdigit() or operand2.lstrip("-").isdigit():
        operand2 = (int(operand2),int(operand2)+1)
    else:
        operand2 = _variables.get(operand2,None)
    
    print operand
    if operand1 is None or operand2 is None:
        return None
    for i in range(*operand1):

        print ("i",i)
        # print (_variables.get(operand2,int(operand2)))
        for j in range(*operand2):
            if operator_symbol=="/" and j==0:
                continue
            result_list.append(operator_mapping[operator_symbol](i,j))
    
    # print (result_list)
    if not result_list:
        return None
    
    print (max(result_list))
    return max(result_list)

def max_result_expression(expression,variables):
    """
    Evaluates the prefix expression and calculates the maximum result for the given variable ranges.

    Arguments:
        expression: the prefix expression to evaluate.
        variables: Keys of this dictionary may appear as variables in the expression.
            Values are tuples of `(min, max)` that specify the range of values of the variable.
            The upper bound `max` is NOT included in the range, so (2, 5) expands to [2, 3, 4].
          
    Returns:
        int:  the maximum result of the expression for any combination of the supplied variables.
        None: in the case there is no valid result for any combination of the supplied variables.
    """
    stack = []
    expression = expression.split()
    space_exist=True
    k=0
    while expression:
        val = expression.pop()
        if val==" ":
            continue
        print (val)
        if val in operator_mapping:
            try:
                op1 = stack.pop()
                op2 = stack.pop()
            except:
                return None
            res = compute(str(op1),str(op2),val,variables)
            if res is None:
                return None
            stack.append(res)
        elif val.isalnum():
            stack.append(val)
        else:
            return None
    
    if not stack or len(stack)>1:
        return None
    return stack.pop()
        
    
    
    raise NotImplementedError("Implement me!")
# if __name__ == '__main__':
#     expression = sys.stdin.readline().strip()
#     variables_raw = sys.stdin.readlines()
    
#     variables = {}

#     for line in variables_raw:
#         line = line.strip()
#         if line:
#             name, lower, upper = line.split()
#             variables[name] = (int(lower), int(upper))
    
#     res = max_result_expression(expression, variables)

#     with open(os.environ['OUTPUT_PATH'], 'w') as f:
#         f.write(str(res) + "\n")


# print (max_result_expression("+ 6 * - 4 + 2 3 8",{ "x": (0, 2), "y": (2, 4) }))
print (max_result_expression("-99",{ "x": (0, 2), "y": (2, 4) }))