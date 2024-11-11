import numpy as np

class MetricsCalculator:
    def __init__(self, waiting_list, service_rate, disease_progression, relapse_rate):
        self.waiting_list = waiting_list  # List of patients
        self.service_rate = service_rate  # Patients served per unit time
        self.disease_progression = disease_progression  # Dict: state -> progression rate
        self.relapse_rate = relapse_rate  # Dict: state -> relapse rate

    def calculate_mean_wait_time(self):
        """
        Calculate the average waiting time
        """
        if not self.waiting_list:
            return 0
        total_wait_time = sum([patient['wait_time'] for patient in self.waiting_list])
        return total_wait_time / len(self.waiting_list)

    def calculate_waiting_list_length(self):
        """
        Calculate the length of the waiting list
        """
        return len(self.waiting_list)

    def calculate_severe_cases(self):
        """
        Calculate the number of severe cases
        """
        severe_cases = [patient for patient in self.waiting_list if patient['state'] == 'severe']
        return len(severe_cases)

    def calculate_relapse_rate_metric(self):
        """
        Calculate the relapse rate
        """
        total_patients = len(self.waiting_list)
        if total_patients == 0:
            return 0
        relapses = sum([1 for patient in self.waiting_list if np.random.rand() < self.relapse_rate.get(patient['state'], 0)])
        return relapses / total_patients
