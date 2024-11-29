// Distribución de stock por categoría
function createCategoryChart() {
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            const categories = ['CD', 'Vinil'];
            const stockData = categories.map(category =>
                data.filter(item => item.formato === category)
                    .reduce((sum, item) => sum + item.stock, 0)
            );

            const ctx = document.getElementById('categoryChart').getContext('2d');
            new Chart(ctx, {
                type: 'pie',
                data: {
                    labels: categories,
                    datasets: [{
                        data: stockData,
                        backgroundColor: ['#4CAF50', '#FF5722']
                    }]
                },
                options: {
                    plugins: {
                        legend: {
                            display: true
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Error:', error));
}

// Ventas por año de lanzamiento
function createTimeChart() {
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            const years = [...new Set(data.map(item => item.anio_lanzamiento))].sort();
            const stockByYear = years.map(year =>
                data.filter(item => item.anio_lanzamiento === year)
                    .reduce((sum, item) => sum + item.stock, 0)
            );

            const ctx = document.getElementById('timeChart').getContext('2d');
            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: years,
                    datasets: [{
                        label: 'Stock Total',
                        data: stockByYear,
                        backgroundColor: '#2196F3'
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Error:', error));
}


function createPriceChart() {
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            const categories = ['CD', 'Vinil'];
            const avgPrice = categories.map(category => {
                const filtered = data.filter(item => item.formato === category);
                return filtered.reduce((sum, item) => sum + item.precio, 0) / filtered.length;
            });

            const ctx = document.getElementById('priceChart').getContext('2d');
            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: categories,
                    datasets: [{
                        label: 'Precio Promedio',
                        data: avgPrice,
                        backgroundColor: ['#673AB7', '#FFC107']
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Error:', error));
}



// Llamada principal
document.addEventListener('DOMContentLoaded', () => {
    createCategoryChart();
    createTimeChart();
    createPriceChart();
});
