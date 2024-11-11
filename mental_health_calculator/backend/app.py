from flask import Flask, request, jsonify
from flask_cors import CORS
from models.population import PopulationDemographics
from models.mental_health import MentalHealthModel
from models.care_pathways import CarePathways
from models.crisis_impact import CrisisImpactModel
from models.metrics import MetricsCalculator
import pandas as pd  # Add this line to import pandas
import numpy as np   # Add this line to import numpy
import json


app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from all domains; consider restricting in production

# Sample data initialization (in practice, should load from a database or config file)
age_distribution = pd.DataFrame({
    'age_group': ['0-18', '19-35', '36-60', '60+'],
    'Population': [100000, 150000, 120000, 80000]
})
gender_ratio = {'male': 0.49, 'female': 0.51}
# Still testing, please ignore this growth_rate_df:
# growth_rate_df = pd.DataFrame({
#     'age_group': ['0-18', '19-35', '36-60', '60+'] * 2,
#     'gender': ['male', 'male', 'male', 'male', 'female', 'female', 'female', 'female'],
#     'growth_rate': [0.01, 0.015, 0.01, 0.005, 0.008, 0.012, 0.009, 0.004]
# })
geographical_distribution = pd.DataFrame({
    'region': ['North', 'South', 'East', 'West'],
    'Population': [100000, 150000, 120000, 80000]
})
economic_status = pd.DataFrame({
    'income_level': ['Low', 'Medium', 'High'],
    'Percentage': [0.3, 0.5, 0.2]
})

# Initialize models
population_model = PopulationDemographics(age_distribution, gender_ratio, geographical_distribution, economic_status)

states = ['mild', 'moderate', 'severe']
transition_matrix = [
    [0.7, 0.2, 0.1],
    [0.1, 0.7, 0.2],
    [0.0, 0.1, 0.9]
]
crisis_adjustments = {
    'unemployment_increase': [1.0, 1.1, 1.2],
    'poverty_increase': [1.0, 1.2, 1.3]
}
mental_health_model = MentalHealthModel(states, transition_matrix, crisis_adjustments)

care_paths = {
    'mild': ['basic_consultation', 'follow_up'],
    'moderate': ['psychotherapy', 'group_therapy', 'follow_up'],
    'severe': ['hospitalization', 'intensive_therapy', 'long_term_follow_up']
}
resource_requirements = {
    'basic_consultation': {'doctor': 1, 'time': 2},
    'follow_up': {'doctor': 1, 'time': 1},
    'psychotherapy': {'psychologist': 2, 'time': 3},
    'group_therapy': {'psychologist': 1, 'time': 2},
    'hospitalization': {'doctor': 3, 'time': 5},
    'intensive_therapy': {'psychologist': 3, 'time': 4},
    'long_term_follow_up': {'doctor': 2, 'time': 3}
}
resource_allocation = {'doctor': 1.0, 'psychologist': 1.0, 'time': 1.0}
care_pathways_model = CarePathways(care_paths, resource_requirements, resource_allocation)

crisis_parameters = {'unemployment_rate': 5, 'poverty_rate': 10, 'immigrant_population': 500}
parameter_adjustments = {
    'unemployment_increase': {'unemployment_rate': 2},
    'poverty_increase': {'poverty_rate': 3},
    'immigration_increase': {'immigrant_population': 200}
}
crisis_impact_model = CrisisImpactModel(crisis_parameters, parameter_adjustments)

relapse_rate = {'mild': 0.1, 'moderate': 0.2, 'severe': 0.3}

# Define API endpoint

@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.json
    # Extract input parameters
    population = data.get('population', 100000)
    crisis_type = data.get('crisis_type', None)
    resource_allocation_input = data.get('resource_allocation', {})
    
    # Update resource allocation strategy
    if resource_allocation_input:
        care_pathways_model.resource_allocation.update(resource_allocation_input)
    
    # Adjust model parameters based on crisis type
    if crisis_type:
        crisis_impact_model.adjust_parameters(crisis_type)
        mental_health_model.adjust_for_crisis(crisis_type)
    
    # Example: Generate waiting list
    waiting_list = []
    for _ in range(population):
        wait_time = np.random.randint(1, 12)  # Wait time (months)
        state = np.random.choice(states, p=mental_health_model.transition_matrix[states.index('mild')])
        waiting_list.append({'wait_time': wait_time, 'state': state})
    
    # Calculate resource needs (example)
    total_resources = {}
    for patient in waiting_list:
        resources = care_pathways_model.calculate_resources(patient['state'])
        for res, qty in resources.items():
            total_resources[res] = total_resources.get(res, 0) + qty
    
    # Calculate metrics
    metrics_calculator = MetricsCalculator(waiting_list, service_rate=100, disease_progression={}, relapse_rate=relapse_rate)
    mean_wait_time = metrics_calculator.calculate_mean_wait_time()
    waiting_list_length = metrics_calculator.calculate_waiting_list_length()
    severe_cases = metrics_calculator.calculate_severe_cases()
    relapse_rate_metric = metrics_calculator.calculate_relapse_rate_metric()
    
    # Build response
    response = {
        'mean_wait_time': mean_wait_time,
        'waiting_list_length': waiting_list_length,
        'severe_cases': severe_cases,
        'relapse_rate': relapse_rate_metric,
        'total_resources': total_resources
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
