d3.csv("data/under.csv").then(function(data) {

  columns = ['Season', 'Team', 'Predicted', 'Playoffs']

  columns.forEach(function(c) {
    d3.select("tr").append('th').text(c)
  })

var tbody = d3.select("tbody")


columns = ['Season', 'Team', 'Predicted', 'Playoffs']

data.forEach(function(team) {
  var row = tbody.append("tr");
  Object.entries(team).forEach(function([key, value]) {
    // console.log(key)
    if (columns.includes(key)) {
    console.log(key)
    var cell = row.append("td");
    cell.text(value);
    }
  });
});


});