d3.csv("data/champs.csv")
    .then(champs => chart(champs))

function chart(csv) {
    var keys = ['Team', 'Rel_Pace', 'Rel_ORtg', 'Rel_DRtg', 'Playoffs']
    let stats = [...new Set(csv.map(champs => champs.teams))]
    var options = d3.select("#stats").selectAll("option")
        .data(stats)
        .enter().append("option")
        .text(champs => champs)

    var svg = d3.select("#chart"),
        margin = { top: 25, bottom: 0, left: 25, right: 25 },
        width = +svg.attr("width") - margin.left - margin.right,
        height = +svg.attr("height") - margin.top - margin.bottom;

    var x = d3.scaleBand()
        .range([0, width])
        .padding(0.4);

    var y = d3.scaleLinear()
        .range([height - margin.bottom, margin.top])

    var xAxis = d3.axisBottom(x).tickSizeOuter(0)
    var yAxis = d3.axisLeft(y)

    svg.append("g")
        .attr("class", "x-axis")
        .attr("transform", `translate(0,${height - margin.bottom})`)
        .call(xAxis);
    svg.append("g")
        .attr("class", "y-axis")
        .attr("transform", `translate(${margin.left},0)`)
        .call(yAxis);

    update(d3.select("#chart").property("value"), 0)

    function update(input, speed) {
        let rawData = csv.filter(f => f.teams == input)[0]
        let champs = []
        for (let i = 0; i < keys.length; i++) {
            let obj = {
                "attribute": keys[i],
                "value": Number(rawData[keys[i]])
            }
            champs.push(obj)
        }

        y.domain([0, d3.max(champs, champs => champs.value) + 5]).nice()
        svg.selectAll(".y-axis").transition().duration(speed)
            .call(yAxis);

        x.domain(champs.map(champs => champs.attribute))
        svg.selectAll(".x-axis").transition().duration(speed)
            .call(xAxis)
        let all_stats = rawData.all_stats_number
        if (all_stats < 10) {
            all_stats = '00' + all_stats
        } else if (all_stats < 100) {
            all_stats = '0' + all_stats
        }
        d3.select("#image").select("img").remove()
        var img = d3.select("#image")
            .append("img")
            .attr("src", `https://images.sportslogos.net/logos/6/225/full/800.gif/img${Team}.png`)
            .attr("width", "300px")
            .attr("height", "300px")

        var tooltip = d3.select("#tooltip")
            .append("div")
            .attr("class", "tooltip")
            .style("opacity", 0);

        let color = {
            'Age': '#88970E',
            'Ht.': '#EF9700',
            'Wt.': '#F5AFF5',
            'FGA': '#CF2701',
            'FG%': '#95A8F5',
            '3PA': '#379D00',
            '3P%': '#ABA493',
            '2PA': '#924494',
            '2P%': '#EA3A73',
            'FTA': '#217FDE',
            'FT%': '#389FCC',
            'ORB': '#FF5733',
            'DRB': '#33FFFA',
            'AST': '#E7FF33',
            'STL': '#E433FF',
            'BLK': '#334AFF',
            'TOV': '#67926F',
            'PF': '#BC0404',
            'PTS': '#FE8D02',

        }

        var bar = svg.selectAll(".bar")
            .champs(champs)
        bar.enter().append("rect")
            .attr("class", "bar")
            .attr("width", x.bandwidth())
            .merge(bar)
            .on("mouseover", function(champs) {
                tooltip.transition()
                    .duration(200)
                    .style("opacity", .9);
                tooltip.html(`<b>${champs.attribute.toUpperCase()}  ${champs.value}`)
                    .style("left", (d3.event.pageX - width / 1.5) + "px")
                    .style("top", (d3.event.pageY - height / 2) + "px")
                    .style("padding", "8px")
                    .style("background-color", "white");
            })
            .on("mouseout", function(champs) {
                tooltip.transition()
                    .duration(500)
                    .style("opacity", 0);
            })
            .transition().duration(speed)
            .attr("x", champs => x(champs.attribute))
            .attr("y", champs => y(champs.value))
            .attr("height", champs => y(0) - y(champs.value))
            .attr("fill", color[rawData.type1])
    }

    var select = d3.select("#stats")
        .on("change", function() {
            update(this.value, 750)
        })

}