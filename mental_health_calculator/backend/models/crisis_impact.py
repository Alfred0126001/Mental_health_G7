class CrisisImpactModel:
    def __init__(self, crisis_parameters, parameter_adjustments):
        self.crisis_parameters = crisis_parameters  # Dict: initial crisis parameters
        self.parameter_adjustments = parameter_adjustments  # Dict: adjustments based on crisis type

    def adjust_parameters(self, crisis_type):
        """
        Adjust model parameters based on the crisis type
        """
        adjustments = self.parameter_adjustments.get(crisis_type, {})
        for param, value in adjustments.items():
            self.crisis_parameters[param] = self.crisis_parameters.get(param, 0) + value
        return self.crisis_parameters

