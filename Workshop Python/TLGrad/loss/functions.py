import jax.numpy as jnp
from jax.scipy.special import logsumexp

def celoss(preds, targets):
    # TODO: preds - output from model of dims (N, 10), targets - labels of dims (N, 10)
    # TODO: implement cross entropy loss
    # TODO: for sum you can use jnp.sum
    # TODO: foer mean you can use jnp.mean
    # TODO: for the log sum exp you can use an arithmetic trick (thanks to computer science)
    #       preds - jax.scipy.special.logsumexp(preds, axis=1, keepdims=True)
    
    return 0
