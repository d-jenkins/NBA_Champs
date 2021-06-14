var svgHeight = 450;
var svgWidth = 1000;
var chartMargin = {
    top: 40,
    bottom: 40,
    left: 100,
    right: 40
};

var chartWidth = svgWidth - (chartMargin.left + chartMargin.right);
var chartHeight = svgHeight - (chartMargin.top + chartMargin.bottom);

var svg = d3
    .select(".container")
    .append("svg")
    .attr("height", svgHeight)
    .attr("width", svgWidth)

var tooltip = d3.select("#tooltip")
    .append("div")
    .attr("class", "tooltip")
    .style("opacity", 0);

var chartGroup = svg.append("g")
    .attr("transform", `translate(${chartMargin.left}, ${chartMargin.top})`);

d3.json("/getdata").then((champs) => {
    console.log(champs);

    champs.forEach((champs) => {
        parseFloat(champs.name);
        //data.team= +data.team;
        //data.chip = +data.chip;
        champs.team = +data.team;
    });

    var xBandScale = d3.scaleBand()
        .domain(champs.map(data => data.name))
        .range([0, chartWidth]);
    //.padding(0);

    var yLinearScale = d3.scaleLinear()
        .domain([0, d3.max(nbaPlayers, data => data.PTS)])
        .range([chartHeight, 0]);

    var bottomAxis = d3.axisBottom(xBandScale);
    var leftAxis = d3.axisLeft(yLinearScale).ticks(20);

    var barSpacing = 10;
    var scaleY = .22;

    var barWidth = (chartWidth - (barSpacing * (nbaPlayers.length - 1))) / nbaPlayers.length;

    chartGroup.append("g")
        .call(leftAxis);
    chartGroup.append("g")
        .attr("transform", `translate(0, ${chartHeight})`)
        .call(bottomAxis);

    chartGroup.selectAll(".bar")
        .data(champs)
        .enter()
        .append("rect")
        .classed("bar", true)
        .attr("width", data => barWidth)
        .attr("height", data => data.team * scaleY)
        .attr("x", (data, i) => i * (barWidth + barSpacing))
        .attr("y", data => chartHeight - data.champs * scaleY);

    chartGroup.append("text")
        .attr("class", "label")
        .attr("y", barHeight / 2)
        .attr("dy", ".35em") //vertical align middle
        .text(function(d) {
            return d.chip;
        }).each(function() {
            labelWidth = Math.ceil(Math.max(labelWidth, this.getBBox().width));
        });

});
