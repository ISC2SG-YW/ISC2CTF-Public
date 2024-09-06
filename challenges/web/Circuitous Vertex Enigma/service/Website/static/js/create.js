var points = []



function roundSf(num,sf){
  var factor = Math.pow(10,sf);
  return Math.round(num*factor)/factor;
}

async function sendBaba(){
  var data = JSON.stringify(points);
  var formData = new FormData();
  formData.append('data',data);
  var response = await fetch(send_baba,{
    method: 'POST',
    body: formData,
  })
  var responseJson = await response.json();
  if ("error" in responseJson){
    alert(responseJson.error);
  }
  else{
    alert(responseJson.data);
  }

}

function initialisePoints(){
  // Make sure there are at least 10 data points and no more than 100
  data = JSON.parse(data);
  var points = [];
  for (var i = 0;i<10;i++){
    points.push({x:roundSf(Math.random()*100,4),
                y:roundSf(Math.random()*100,4)});
  }
  // This extend function overwrites the random points with the data from the URL, 
  // but still makes sure there are at least 10 datapoints inside!
  $C.extend(true,points,data);
  var collectionArr = $C(points);
  return collectionArr.get({
    filter: (el)=>el.x>=0 && el.x<=100 && el.y>=0 && el.y<=100,
    count:100,
    }
  );
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

function updateUrl(points){
  var data = JSON.stringify(points);
  var url = new URL(window.location.href);
  url.searchParams.set('data',data);
  window.history.pushState({}, '', url);
}
function intialisePage(points){
  // Register the Scatter Plot component
  Vue.component('scatter-plot', {
    extends: VueChartJs.Scatter,
    data() {
      return {
        scatterData: points,
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
        const xValue = roundSf(xScale.getValueForPixel(event.offsetX),4);
        const yValue = roundSf(yScale.getValueForPixel(event.offsetY),4);
        // Add the new point to the scatter data
        this.scatterData.push({ x: xValue, y: yValue });
        // Update the URL
        updateUrl(this.scatterData);

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
}
  
window.onload = function(){
  points = initialisePoints();
  intialisePage(points);
  document.querySelector("#send").onclick = sendBaba;
}