<html>
<head>
    <title>State Input</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <h1>Enter a State Name</h1>
    <form id="stateForm">
        <input type="text" id="stateInput" placeholder="Enter a state name">
        <button type="submit">Submit</button>
    </form>
    <div id="result">
        <!-- The result from the backend will be displayed here -->
        <h2 id="chartTitle"></h2>
        <canvas id="barChart"></canvas>
    </div>

<script>
        // Listen for the form submission
        document.getElementById('stateForm').addEventListener('submit', function (e) {
            e.preventDefault(); // Prevent the default form submission
            // Get the state name from the input field
            const stateName = document.getElementById('stateInput').value;
            // Send the stateName to the backend using a fetch request
            fetch(`http://localhost:5000/api/data/state/${stateName}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                }
            })
            .then(response => response.json())
            .then(data => {
                // Get the total population and deaths from lung cancer
                const totalPopulation = data['TotalPopulation'];
                const deathCount = data['Total amount of death from lung cancer'];

                // Display the chart
                const chartTitle = `Total Population vs Deaths from Lung Cancer in ${stateName}`;
                document.getElementById('chartTitle').textContent = chartTitle;
                new Chart(document.getElementById('barChart'), {
                    type: 'bar',
                    data: {
                        labels: ['Total Population', 'Deaths from Lung Cancer'],
                        datasets: [{
                            data: [totalPopulation, deathCount],
                            backgroundColor: ['lightblue', 'red'],
                            borderWidth: 1,
                        }],
                    },
                    options: {
                        scales: {
                            y: {
                                beginAtZero: true,
                            },
                        },
                    },
                });
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    </script>
</body>
</html>
