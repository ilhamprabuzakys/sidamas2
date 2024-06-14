const Chart = {
    props: ["width", "height"],
    template: `
        <canvas id="chartKepuasan" :width="width" :height="height"></canvas>
    `,
    mounted() {
        this.initializeChart();
    },
    methods: {
        initializeChart() {
            let chartContainer = document.getElementById("chartKepuasan");
            let chart = new Chart(chartContainer, {
                type: "bar",
                data: {
                    labels: [
                        "Tidak Puas",
                        "Kurang Puas",
                        "Puas",
                        "Sangat Puas",
                    ],
                    datasets: [
                        {
                            label: "Kepuasan Responden",
                            data: [12, 9, 17, 22],
                            backgroundColor: [
                                "rgba(255, 99, 132, 0.2)",
                                "rgba(54, 162, 235, 0.2)",
                                "rgba(255, 206, 86, 0.2)",
                                "rgba(75, 192, 192, 0.2)",
                            ],
                            borderColor: [
                                "rgba(255,99,132,1)",
                                "rgba(54, 162, 235, 1)",
                                "rgba(255, 206, 86, 1)",
                                "rgba(75, 192, 192, 1)",
                            ],
                            borderWidth: 1,
                        },
                    ],
                },
            });
        },
    },
};

export default Chart;
