<script>
        var ctx = document.getElementById('GeracaoEnergia').getContext('2d');
        var chart = new Chart(ctx, {
            // The type of chart we want to create
            type: 'bar',
    
            // The data for our dataset
            data: {
                labels: {{ meses_ano|safe }},
                datasets: [{
                    label: 'Geração anual',
                    backgroundColor: 'rgb(255, 99, 132)',
                    borderColor: 'rgb(255, 99, 132)',
                    data: {{ energia_gerada_final }}
                }]
            },
    
            // Configuration options go here
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        },
                        scaleLabel: {
                            display: true,
                            labelString: 'kWh'
                        }
                    }]
                }
            }
        });
    </script>

<script>
    var ctx = document.getElementById('Ganho por mês').getContext('2d');
    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'bar',

        // The data for our dataset
        data: {
            labels: {{ meses_ano|safe }},
            datasets: [{
                label: 'Ganho mensal',
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: {{ arrecadacao_mensal }}
            }]
        },

        // Configuration options go here
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    },
                    scaleLabel: {
                        display: true,
                        labelString: 'Reais'
                    }
                }]
            }
        }
    });
</script>