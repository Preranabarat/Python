import inspect

def example_function(param1, param2, param3='default', *args, **kwargs):
    pass

def get_parameter_names(func):
    # Get the signature of the function
    signature = inspect.signature(func)
    
    # Get the parameter names from the signature
    parameter_names = list(signature.parameters.keys())
    
    return parameter_names

# Example usage
param_names = get_parameter_names(example_function)
print("Parameter names:",param_names)