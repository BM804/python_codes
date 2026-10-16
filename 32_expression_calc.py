"""Distinct Python example #32."""
import ast,operator
ops={ast.Add:operator.add,ast.Sub:operator.sub,ast.Mult:operator.mul,ast.Div:operator.truediv}
def calc(n):
 if isinstance(n,ast.Expression):return calc(n.body)
 if isinstance(n,ast.Constant) and type(n.value) in (int,float):return n.value
 if isinstance(n,ast.BinOp) and type(n.op) in ops:return ops[type(n.op)](calc(n.left),calc(n.right))
 raise ValueError("Only simple arithmetic is allowed")
print(calc(ast.parse(input("expression: "),mode="eval")))
