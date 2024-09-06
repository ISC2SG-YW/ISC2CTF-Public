const process = require('process');
const fs = require('fs');
const flag = fs.readFileSync('./backend/flag.txt', 'utf8');

try {
    // Parse the provided data and process it
    const encodedData = process.argv[2];
    var grid = []
    const {size,grid:requestGrid} = JSON.parse(encodedData);
    for (var i = 0; i < size; i++) {
        var row = []
        for (var j = 0; j < size; j++) {
            row.push(0)
        }
        grid.push(row)
    }
    for (var cell of requestGrid) {
        grid[cell.x][cell.y] = cell.value
    }
    for (var row of grid) {
        for (var cell of row) {
            if (cell > 2048 || typeof cell != "number") {
                console.log("Hey! No Cheating :C")
                process.exit(1);
            }
        }
    }

    var score = 0
    for (var i = 0;i<4;i++){
        for (var j = 0;j<4;j++){
            score += grid[i][j]
        }
    }

    if (score >= 1048576){
        console.log(
            JSON.stringify({
            message: `Wow! You're so good at this game! Here's the flag: ${flag}`,
            score: score,
            success: true
        }))
    }
    else{
        console.log(JSON.stringify({
            score: score,
            success: false
        }))
    }

} catch (error) {
    console.log("Error processing data:", error.message);
    process.exit(1);
}

