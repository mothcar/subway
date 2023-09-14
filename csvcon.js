var fs = require('fs');

var data = fs.readFileSync('./777.csv')
    .toString() // convert Buffer to string
    .split('\n') // split string to lines
    .map(e => e.trim()) // remove white spaces for each line
    // .map(e => e.split(',').map(e => e.trim())); // split each line to array
    .map(e => e.split(','))
    .map(e=>{
        if(e[2] == undefined) return 
        if(e[2].includes("GEOMETRYCOLLECTION")) {
            // console.log(e[2])
        } else {
            console.log(e)
            return e
        }
    })
    .map(e=>{
        console.log(e)
        
        // if(e[2].includes("id")) return 
        if(e) {
            // console.log(e[2])
            let start = e[2].indexOf('(')
            let end = e[2].indexOf(" ", start+1);
            let final = e[2].indexOf(')')
            // console.log(start)
            // console.log(end)
            let lng = e[2].substring(start+1, end)
            let lat = e[2].substring(end, final)
            return [Number(lat),Number(lng)]
        } else {
            return
        }
        
        
    })
    // .map(e => e.split(',').map(e => e.trim())); // split each line to array
    // .map(e => e.trim())

console.log(data);
// console.log(JSON.stringify(data, '', 2)); // as json
let dictstring = JSON.stringify(data, '', 2)
var fs = require('fs');
fs.writeFile("./thing.json", dictstring, function(err, result) {
    if(err) console.log('error', err);
});