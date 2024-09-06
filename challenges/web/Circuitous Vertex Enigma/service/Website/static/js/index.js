async function addPointToDatabase(x,y){
    var formData = new FormData();
    formData.append('x', x);
    formData.append('y', y);
    fetch(add_url, {
      method: 'POST',
      body: formData,
    })
  }
  function calculateBestFitLine(data) {
    const n = data.length;
    let sumX = 0, sumY = 0, sumXY = 0, sumXX = 0;

    data.forEach(point => {
      sumX += point.x;
      sumY += point.y;
      sumXY += point.x * point.y;
      sumXX += point.x * point.x;
    });

    const slope = (n * sumXY - sumX * sumY) / (n * sumXX - sumX * sumX);
    const intercept = (sumY - slope * sumX) / n;

    const xMin = Math.min(...data.map(point => point.x));
    const xMax = Math.max(...data.map(point => point.x));

    return [
      { x: xMin, y: slope * xMin + intercept },
      { x: xMax, y: slope * xMax + intercept }
    ];
  }
  // Register the Scatter Plot component
  Vue.component('scatter-plot', {
    extends: VueChartJs.Scatter,
    data() {
      return {
        scatterData: scatterData,
        bestFitLine: [],
        chartOptions: {
          responsive: true,
          animation:false,
          maintainAspectRatio: false,
          legend: {
            display: false // This hides the legend
          },
          scales: {
            xAxes: [{ type: 'linear', position: 'bottom' }]
          },
          onClick: (event, elements) => {
            // Custom onClick handler to add points
            this.addPoint(event);
          }
        }
      };
    },
    computed: {
      chartData() {
        // Calculate the best fit line based on the scatter data

        return {
          datasets: [
            {
              label: 'Scatter Data',
              backgroundColor: '#f87979',
              data: this.scatterData,
              showLine: false,
            },
            {
              label: 'Best Fit Line',
              borderColor: '#36a2eb',
              data: this.bestFitLine,
              type: 'line',
              fill: false,
              pointRadius: 0,
              borderWidth: 2,
            }
          ]
        };
      }
    },
    methods: {
      addPoint(event) {
        // Get the chart instance
        const chart = this.$data._chart;

        // Get the x and y axis
        const xScale = chart.scales['x-axis-1'];
        const yScale = chart.scales['y-axis-1'];

        // Get the coordinates of the click event
        const xValue = xScale.getValueForPixel(event.offsetX);
        const yValue = yScale.getValueForPixel(event.offsetY);
        addPointToDatabase(xValue, yValue);
        // Add the new point to the scatter data
        this.scatterData.push({ x: xValue, y: yValue });

        // Recalculate the best fit line
        this.bestFitLine = calculateBestFitLine(this.scatterData);
        // Update the chart to reflect the new data
        this.renderChart(this.chartData, this.chartOptions);
        
      }
    },
    mounted() {
      // Render the chart
      this.bestFitLine = calculateBestFitLine(this.scatterData);
      this.renderChart(this.chartData, this.chartOptions);
    }
  });

  // Main Vue Instance
  new Vue({
    el: '#main-app',
    data: {
      dynamicComponentVisible: false
    },

  });