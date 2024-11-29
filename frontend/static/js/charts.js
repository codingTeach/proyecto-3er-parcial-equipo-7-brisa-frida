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

function createPriceDistributionChart() {
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            const categories = ['CD', 'Vinil'];
            const avgPrice = categories.map(category => {
                const filtered = data.filter(item => item.formato === category);
                return filtered.reduce((sum, item) => sum + item.precio, 0) / filtered.length;
            });
            const ctx = document.getElementById('priceDistributionChart').getContext('2d');
            new Chart(ctx, {
                type: 'pie',
                data: {
                    labels: categories,
                    datasets: [{
                        data: avgPrice,
                        backgroundColor: ['#FF9800', '#9C27B0']
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

function createStockEvolutionChart() {
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            const years = [...new Set(data.map(item => item.anio_lanzamiento))].sort();
            const stockByYear = years.map(year =>
                data.filter(item => item.anio_lanzamiento === year)
                    .reduce((sum, item) => sum + item.stock, 0)
            );
            const ctx = document.getElementById('stockEvolutionChart').getContext('2d');
            new Chart(ctx, {
                type: 'line',
                data: {
                    labels: years,
                    datasets: [{
                        label: 'Stock Total',
                        data: stockByYear,
                        borderColor: '#4CAF50',
                        fill: false
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

function createTotalStockByFormatChart() {
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            const formats = ['CD', 'Vinil'];
            const stockByFormat = formats.map(format =>
                data.filter(item => item.formato === format)
                    .reduce((sum, item) => sum + item.stock, 0)
            );
            const ctx = document.getElementById('totalStockByFormatChart').getContext('2d');
            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: formats,
                    datasets: [{
                        label: 'Total de Stock',
                        data: stockByFormat,
                        backgroundColor: ['#FF5722', '#8BC34A']
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

document.addEventListener('DOMContentLoaded', () => {
    createCategoryChart();
    createTimeChart();
    createPriceChart();
    createPriceDistributionChart();
    createStockEvolutionChart();
    createTotalStockByFormatChart();
});
