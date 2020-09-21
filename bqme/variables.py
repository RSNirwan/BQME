class Variable:
    """
    Base class for different kind of variables
    """
    def __init__(self, value, name, lower, upper):
        self.lower = lower
        self.upper = upper
        self.name = name
        self.value = self.approve(value)

    def approve(self, value):
        if self.lower < value < self.upper:
            return value
        else:
            raise ValueError(f'Input parameter "{self.name}" needs to be in range ({self.lower}, {self.upper}), currently set to {value}.')


class ContinuousVariable(Variable):
    """
    container for continuous variables (-inf, inf)
    """
    def __init__(self, value, name):
        lower = float('-inf')
        upper = float('inf')
        super().__init__(value, name, lower, upper)


class PositivContinuousVariable(Variable):
    """
    container for positive continous variables (0, inf)
    """
    def __init__(self, value, name):
        lower = 0
        upper = float('inf')
        super().__init__(value, name, lower, upper)


