if (process.argv.length < 3) {
    console.log('Usage: analyze.js file.js');
    process.exit(1);
}
var fs = require('fs'),
    esprima = require('esprima');
var filename = process.argv[2];
var code = fs.readFileSync(filename, 'utf-8');
ast = JSON.stringify(esprima.parse(code), null, 2);
console.log(ast);


//function analyzeCode(code) {
//    var ast = esprima.parse(code);
////    console.log(ast);
////    console.log(code);
//
//}
//
//// 2
//if (process.argv.length < 3) {
//    console.log('Usage: analyze.js file.js');
//    process.exit(1);
//}

//// 3
//var filename = process.argv[2];
//console.log('Reading ' + filename);
//var code = fs.readFileSync(filename, 'utf-8').toString();
////console.log(code);
//var ast = esprima.parse(code);
//console.log(ast);
//
//
//analyzeCode(code);
//console.log('Done');

//var esprima = require('esprima');
//const fs = require('fs')
//
//const l = console.log
//
//const path = process.argv[2]
////const name = process.argv[3]
//
//const buffer = fs.readFileSync(path).toString()
//
//ast = JSON.stringify(esprima.parse(buffer), null, 2);
//l(ast);
////tokenized = JSON.stringify(esprima.tokenize(buffer), null, 2);
//
////fs.writeFile('../data/ast/' + name + '.json', ast, (err) => {
////  if (err) throw err;
////  //console.log('AST written to file');
////});
////fs.writeFile('ast.csv', ast);
//
////fs.writeFile('../data/tokenized/' + name + '.json', ast, (err) => {
////  if (err) throw err;
////  //console.log('Tokens written to file');
////});
//
////l(name + " written to file")