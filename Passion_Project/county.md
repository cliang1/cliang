[**Home Page**](/index.md)
<html>
<head>
    <title>County and State Input</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.7.0/chart.min.js"></script>
</head>
<body>
    <h1>Enter a County Name!</h1>
    <!--create a title-->
    <form id="countyForm">
        <input type="text" id="countyInput" placeholder="Enter a county name">
        <!--create the box to enter the county name-->
        <button type="submit">Submit</button>
        <!--create the button people press to get the data-->
    </form>
    <div id="countyResult">
        <!-- The result for county data from the backend will be displayed here -->
    </div>
    <div id="countyPieChart">
        <!-- The pie chart for county data will be displayed here -->
    </div>
    <script>
        // County Form Submission
        document.getElementById('countyForm').addEventListener('submit', function (e) {
            e.preventDefault();
            //prevents the submit button from simply "submitting form", allows user to do what they want with the user input after the button is pressed using JS
            const countyName = document.getElementById('countyInput').value;
            fetch(`http://localhost:5000/api/data/county/county/${countyName}`, 
            //spreifies that this is for couty names in the database called county within the api folder
            {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                }
            })
            .then(response => {
                if (response.status === 404) {
                    return { error: "County data not found" };
                    //makes sure the data actually exists
                }
                return response.json();
            })
            .then(data => {
                if (data.error) {
                    document.getElementById('countyResult').textContent = `Error: ${data.error}`;
                } else {
                    // Create the pie chart for county data
                    const pieChartHtml = `
                        <h2>Air Pollution in ${data.County}</h2>
                        <canvas id="countyAirPollutionChart"></canvas>
                    `;
                    document.getElementById('countyPieChart').innerHTML = pieChartHtml;
                    new Chart(document.getElementById('countyAirPollutionChart'), {
                        type: 'pie',
                        data: {
                            labels: ['Good Days', 'Moderate Days', 'Unhealthy Days', 'Very Unhealthy Days', 'Hazardous Days'],
                            //uses all the categories from the csv file
                            datasets: [{
                                data: [data['Good Days'], data['Moderate Days'], data['Unhealthy Days'], data['Very Unhealthy Days'], data['Hazardous Days']],
                                backgroundColor: ['green', 'yellow', 'orange', 'red', 'purple'],
                                //organizes the legend
                            }],
                        },
                        options: {
                            plugins: {
                                tooltip: {
                                    callbacks: {
                                        label: function (context) {
                                            const label = context.label || '';
                                            const value = context.parsed || 0;
                                            const total = context.dataset.data.reduce((acc, val) => acc + val, 0);
                                            const percentage = ((value / total) * 100).toFixed(2);
                                            return `${label}: ${percentage}%`;
                                        },
                                    },
                                },
                            },
                            //creates a tooltip that displays the percentage of the total days that each category take up on the graph
                            title: {
                                display: true,
                                text: `Air Pollution in ${data.County}`,
                            },
                        },
                    });
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    </script>
</body>
</html>