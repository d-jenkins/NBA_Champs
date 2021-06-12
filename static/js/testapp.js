d3.csv("data/champs.csv").then(function(nbaTeams) {

    console.log(nbaTeams);

    // log a list of names
    var names = nbaTeams.map(data => data.name);
    console.log("names", names);

    //
    teamData.forEach(function(data) {
        data.chip = +data.chip;
        console.log("Name:", data.name);
        console.log("Chip?:", data.chip);
    });
}).catch(function(error) {
    console.log(error);
});
