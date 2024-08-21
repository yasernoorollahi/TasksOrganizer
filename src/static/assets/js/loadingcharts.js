async function fetchDataAndRenderChart() {
  try {
    const response = await fetch('/dashboard/chart-data');
    const data = await response.json();
    const options = {
      series: [
        {
          name: 'Task Names',
          data: data.values, // Use the fetched data
        },
        //adding completed tasks
        // {
        //   name: 'Completed Tasks:',
        //   data: data.values,
        // },
      ],
      chart: {
        type: 'bar',
        height: 350,
      },
      xaxis: {
        categories: data.labels, // Use the fetched labels
      },
    };

    const chart = new ApexCharts(document.querySelector('#chart'), options);

    chart.render();
  } catch (error) {
    console.error('Error fetching chart data', error);
  }
}

fetchDataAndRenderChart();
