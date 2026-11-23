import torch

def flatten_then_reshape(x: torch.Tensor, new_shape) -> torch.Tensor:
    # TODO: flatten x to 1-D, then rearrange into new_shape
    x = torch.tensor(x)
    flat = x.flatten()
    return flat.reshape(new_shape)

    pass

def transpose_last_two(x: torch.Tensor) -> torch.Tensor:
    xt = x.transpose(-2,-1)
    return xt
    pass
