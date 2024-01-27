//chart data here
var data = {
    labels:['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    datasets: [
      {
        label: 'Collected Rainwater',
        backgoundColor: 'rgba(75, 192, 192, 0.7)',
        data: [0,0,10,4,1,0,0]
      },
      {
        label: 'Tap Water Used',
        backgoundColor: 'rgba(255, 99, 132, 0.7)',
        data: [3,3,0,0,0,0,0]
      },
      {
        label: 'Total Water Used',
        backgoundColor: 'rgba(255, 206, 86, 0.7)',
        data: [3,3,3,3,3,3]
      }
    ]
  };

  //chart options here
  var chartOptions = {
    responsive: true,
    scales: {
      x: {
        stacked: false
      },
      y: {
        stacked: false
      }
    }
  };

  //canvas element
  var ctx = document.getElementById('rwUsageChart').getContext('2d');

  //actual bar chart
  var rwStatsChart = new Chart(ctx, {
    type: 'bar',
    data: data,
    options: chartOptions
  });