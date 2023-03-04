import numpy as np
import theano
import theano.tensor as T

# Define the mathematical expression
x = T.dscalar('x')
y = T.dscalar('y')
z = x ** 2 + y ** 2

# Compile the expression into a function
f = theano.function(inputs=[x, y], outputs=z)

# Evaluate the function on some input values
result = f(1.0, 2.0)

print(result)  # Output: 5.0
