// script.js
document.getElementById('calculator-form').addEventListener('submit', async function(event) {
    event.preventDefault(); // Prevent the default form submission behavior

    // Get input values
    let population = parseInt(document.getElementById('population').value) || 0;
    let crisisType = document.getElementById('crisis-type').value;
    let doctorAllocation = parseFloat(document.getElementById('doctor-allocation').value) || 1.0;
    let psychologistAllocation = parseFloat(document.getElementById('psychologist-allocation').value) || 1.0;
    let timeAllocation = parseFloat(document.getElementById('time-allocation').value) || 1.0;

    let resourceAllocation = {
        'doctor': doctorAllocation,
        'psychologist': psychologistAllocation,
        'time': timeAllocation
    };

    // Build request data
    let requestData = {
        population: population,
        crisis_type: crisisType,
        resource_allocation: resourceAllocation
    };

    try {
        // Display loading status
        document.getElementById('mean-wait-time').innerText = 'Loading...';
        document.getElementById('waiting-list-length').innerText = 'Loading...';
        document.getElementById('severe-cases').innerText = 'Loading...';
        document.getElementById('relapse-rate').innerText = 'Loading...';

        let response = await fetch('http://127.0.0.1:5000/api/calculate', { // Point to the local backend
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestData)
        });

        if (!response.ok) {
            throw new Error('Network response was not OK');
        }

        let data = await response.json();

        // Update the front-end display
        document.getElementById('mean-wait-time').innerText = data.mean_wait_time.toFixed(2) + ' months';
        document.getElementById('waiting-list-length').innerText = data.waiting_list_length;
        document.getElementById('severe-cases').innerText = data.severe_cases;
        document.getElementById('relapse-rate').innerText = (data.relapse_rate * 100).toFixed(2) + ' %';
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred during the calculation. Please try again later.');
        // Reset display
        document.getElementById('mean-wait-time').innerText = '-';
        document.getElementById('waiting-list-length').innerText = '-';
        document.getElementById('severe-cases').innerText = '-';
        document.getElementById('relapse-rate').innerText = '-';
    }
});

