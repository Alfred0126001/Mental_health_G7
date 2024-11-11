import numpy as np

class MentalHealthModel:
    def __init__(self, states, transition_matrix, crisis_adjustments=None):
        self.states = states
        self.transition_matrix = np.array(transition_matrix)
        self.crisis_adjustments = crisis_adjustments

    def adjust_for_crisis(self, crisis_type):
        """
        Adjust the transition matrix based on the crisis type
        """
        if self.crisis_adjustments and crisis_type in self.crisis_adjustments:
            adjustment = self.crisis_adjustments[crisis_type]
            self.transition_matrix = self.transition_matrix * adjustment
            # Re-normalize the transition matrix
            self.transition_matrix = self.transition_matrix / self.transition_matrix.sum(axis=1, keepdims=True)

    def simulate_progression(self, current_state, steps):
        """
        Simulate disease progression
        """
        state_index = self.states.index(current_state)
        progression = [current_state]
        for _ in range(steps):
            state_index = np.random.choice(len(self.states), p=self.transition_matrix[state_index])
            progression.append(self.states[state_index])
        return progression
