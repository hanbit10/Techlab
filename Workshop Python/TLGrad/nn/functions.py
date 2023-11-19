import jax.numpy as jnp


"""
    Linear transformation 
    y = x * A + b 

    with:
    y       = output [output_dim]jjjj
    x       = input [input_dim]
    A       = parameter Matrix [input_dim, output_dim]
    b       = bias [output_dim]
"""
def linear(x, A, b):
    # TODO: x - input, A - parameter matrix, b - bias
    # TODO: implement the linear transformation, use .dot for the multiplication
    # TODO: return y
    y = jnp.dot(x * A) + b
    
    return y
