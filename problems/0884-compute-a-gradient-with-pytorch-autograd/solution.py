import torch

def grad_of_quadratic(x_value: float) -> float:
    # TODO: build a tracked leaf for x, compute f(x), run backprop, return df/dx as a float
    x = torch.tensor(x_value,requires_grad = True) #leaf
    y = x**2 + 3*x +2 #notaleaf
    y.backward() #works backward through those recorded steps and calculates the derivative. The result is stored on x in x.grad. It doesn’t return anything.
    return x.grad.item()

    pass

#requires_grad=True tells autograd to track operations on this tensor and store a gradient for it.

