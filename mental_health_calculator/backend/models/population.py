import pandas as pd

class PopulationDemographics:
    def __init__(self, age_distribution, gender_ratio, geographical_distribution, economic_status):
        self.age_distribution = age_distribution  # DataFrame containing age group distribution
        self.gender_ratio = gender_ratio          # Dict with gender ratio
        self.geographical_distribution = geographical_distribution  # DataFrame with geographical distribution
        self.economic_status = economic_status    # DataFrame with economic status distribution

    def project_population(self, years, growth_rate):
        """
        Project future population based on growth rate
        """
        future_population = self.age_distribution.copy()
        future_population['Population'] = future_population['Population'] * ((1 + growth_rate) ** years)
        return future_population
