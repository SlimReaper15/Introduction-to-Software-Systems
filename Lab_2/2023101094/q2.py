import sympy

def multiply(expression):
    # Split the expression into two polynomials
    expression = [poly.strip("()") for poly in expression.split(")(")]
    
    poly1, poly2 = expression
    poly1 = poly1.replace("x", "*x").replace("+*", "+").replace("-*", "-")
    poly1 = poly1.replace("^", "**").strip("*")

    poly2 = poly2.replace("x", "*x").replace("+*", "+").replace("-*", "-")
    poly2 = poly2.replace("^", "**").strip("*")
    
    poly1 = sympy.sympify(poly1)
    poly2 = sympy.sympify(poly2)

    # Multiply and expand the polynomials
    product = sympy.expand(poly1 * poly2)

    # Replace '**' with '^' and cleanup multiplication with x
    result = str(product).replace('**', '^').replace('*x', 'x')

    return result

expression = input("Enter expression: ")

# Perform multiplication and expansion
result = multiply(expression)

# Display the result
print("Result:", result)