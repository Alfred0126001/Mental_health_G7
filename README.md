# Mental Health Service Resource Planning Calculator

This project is designed to serve as a resource planning calculator for mental health services, focusing on predicting and managing resources needed based on population demographics, crisis scenarios, and health progression models.

## Project Structure

```plaintext
mental_health_calculator/
├── backend/
│   ├── app.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── population.py
│   │   ├── mental_health.py
│   │   ├── care_pathways.py
│   │   ├── crisis_impact.py
│   │   └── metrics.py
│   ├── requirements.txt
│   └── config.py
├── frontend/
│   ├── index.html
│   ├── styles.css
│   ├── script.js
│   └── assets/
│       └── ... (images, icons, etc.)
└── README.md
```

## Backend

The backend folder contains the server-side code and logic for the application, including API endpoints and data processing models.

- **app.py**: The main application file for the backend. This file sets up the Flask API server, configures CORS, initializes the models, and defines the API endpoints for the frontend to interact with.
  
- **models/**: This directory contains all the core Python modules that define the different models and calculations for the application.
  
  - **\_\_init\_\_.py**: Marks this folder as a Python package.
  
  - **population.py**: Defines the `PopulationDemographics` class, which handles population data, including age distribution, gender ratio, geographical distribution, and economic status. It includes methods for projecting future population sizes based on growth rates.
  
  - **mental_health.py**: Contains the `MentalHealthModel` class, which models the progression of mental health states across a population. It allows for state transitions, adjustments due to crisis scenarios, and the simulation of health progression.
  
  - **care_pathways.py**: Implements the `CarePathways` class, defining different pathways for mental health care based on severity levels (e.g., mild, moderate, severe). It also calculates the resources required for each care pathway.
  
  - **crisis_impact.py**: Defines the `CrisisImpactModel` class, which adjusts model parameters based on various crisis scenarios (e.g., increased unemployment, poverty, immigration) and simulates how these changes impact resource needs.
  
  - **metrics.py**: Contains the `MetricsCalculator` class, which calculates various metrics such as mean wait time, waiting list length, severe cases, and relapse rate based on real data.
  
- **requirements.txt**: Lists all Python dependencies needed to run the backend (e.g., Flask, NumPy, pandas). Run `pip install -r requirements.txt` to install these dependencies.

- **config.py**: Contains configuration settings for the backend application, such as database connections, environment settings, and other constants used across the backend.

## Frontend

The frontend folder contains the client-side code, including HTML, CSS, JavaScript, and any other assets.

- **index.html**: The main HTML file for the user interface. It provides a form to input parameters, such as population size, crisis type, and resource allocation adjustments, and displays the calculated results.

- **styles.css**: The main CSS file for styling the frontend UI, ensuring a consistent look and feel.

- **script.js**: The main JavaScript file for the frontend logic. It handles form submission, fetches data from the backend API, and updates the HTML elements to display the calculated results.

- **assets/**: A folder that contains images, icons, or other media assets used in the frontend.

## Usage

1. **Setup and Install Dependencies**:
   - Navigate to the `backend` directory and install dependencies using:
     ```bash
     pip install -r requirements.txt
     ```

2. **Run the Backend Server**:
   - Start the Flask server from the `backend` directory:
     ```bash
     python app.py
     ```
   - The server will be accessible at `http://127.0.0.1:5000`.

3. **Open the Frontend**:
   - Open `index.html` in a web browser, or use the Live Server extension in VSCode to serve the frontend.

4. **Use the Calculator**:
   - Input the parameters in the form and submit. The frontend will send a request to the backend, which processes the data and returns results such as mean wait time, waiting list length, severe cases, and relapse rate.

