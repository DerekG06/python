# Includes both modules calculator and geometry
from math_operations import calculator, geometry

result = calculator.add(5, 3)
print("Addition result:", result)

result = calculator.subtract(10, 4)
print("Subtraction result:", result)

result = geometry.circle_area(5)
print("Circle area:", result)

result = geometry.rectangle_area(3, 8)
print("Rectangle Area:", result)
