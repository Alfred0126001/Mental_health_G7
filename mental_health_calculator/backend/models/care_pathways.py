class CarePathways:
    def __init__(self, care_paths, resource_requirements, resource_allocation):
        self.care_paths = care_paths  # Dict: state -> list of care steps
        self.resource_requirements = resource_requirements  # Dict: step -> resource requirements
        self.resource_allocation = resource_allocation  # Dict: resource type -> allocation ratio

    def calculate_resources(self, state):
        """
        Calculate the resources required based on the patient's condition state
        """
        steps = self.care_paths.get(state, [])
        total_resources = {}
        for step in steps:
            resources = self.resource_requirements.get(step, {})
            for res, qty in resources.items():
                total_resources[res] = total_resources.get(res, 0) + qty
        # Apply resource allocation strategy
        allocated_resources = {res: qty * self.resource_allocation.get(res, 1) for res, qty in total_resources.items()}
        return allocated_resources

