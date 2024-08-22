async function fetchDataAndRenderChart() {
  try {
    const response = await fetch('/dashboard/chart-data');
    const data = await response.json();
    const options = {
      chart: {
        type: 'bar',
        height: 350,
      },
      colors: ['#5D87FF', '#4CAF50'],
      series: [
        {
          name: 'Tasks',
          data: data.values,
        },
        {
          name: 'completed tasks',
          data: [30, 7, 17, 3],
        },
      ],
      xaxis: {
        categories: data.labels,
      },
    };

    const chart = new ApexCharts(document.querySelector('#chart'), options);

    chart.render();
  } catch (error) {
    console.error('Error fetching chart data', error);
  }
}

fetchDataAndRenderChart();
