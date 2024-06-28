class Solution:
  def multiply(self, num1: str, num2: str) -> str:
    formula: str = f"{num1} * {num2}"
    return str(eval(formula))
