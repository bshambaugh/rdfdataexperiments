// https://github.com/RubenVerborgh/N3.js

// code from:: https://www.codementor.io/codementorteam/how-to-use-json-files-in-node-js-85hndqt32
//Define JSON File
var fs = require('fs');
// get the content from the file
var contents = fs.readFileSync('countries.json');
// Define to JSON type
var jsonContent = JSON.parse(contents);

function servicetoTTL(content) {

  var countryinfo = '';
  var result = '';
  for(var exKey in jsonContent) {
     var countryinfo = '';
     var neighbors = '';

      if(jsonContent[exKey]['region'] == 'Africa') {
       // I need to add some cascading effect ....
   
   if(jsonContent[exKey]['borders'].length != 0) {
         var countryinfo = 'Country:'+jsonContent[exKey]['name']['common'].replace(/ /g,'_') 
          + ' :hasRegion  ' + '\'' + jsonContent[exKey]['region'] 
          + '\'' + '; :hasSubRegion ' + '\'' + jsonContent[exKey]['subregion'] 
          + '\'' + '; :hasCode ' +'\'' + jsonContent[exKey]['cca3'] + '\'' + ' ; ';
} else {
         var countryinfo = 'Country:'+jsonContent[exKey]['name']['common'].replace(/ /g,'_') 
         + ' :hasRegion  ' + '\'' + jsonContent[exKey]['region'] + '\'' + '; :hasSubRegion ' 
         + '\'' + jsonContent[exKey]['subregion'] + '\'' 
         + '; :hasCode ' +'\'' + jsonContent[exKey]['cca3'] + '\'' + ' . ';

}      
      
 //  var neighbors = '';
         for(var exKey2 in jsonContent[exKey]['borders']) {
             if(exKey2 < jsonContent[exKey]['borders'].length - 1) {
                neighbors = neighbors + ':neighborOf' + ' :' + jsonContent[exKey]['borders'][exKey2] + ' ; ';
             } else {
                neighbors = neighbors + ':neighborOf' + ' :' + jsonContent[exKey]['borders'][exKey2] + ' . ';
             }
         }

          result = result + countryinfo + neighbors;
    }
     //     result = result + countryinfo + neighbors;
 }

     return result;
}

console.log(servicetoTTL(jsonContent));




