var MongoClient = require('mongodb').MongoClient
var fs = require('fs')
var url = "mongodb://crawler:pwp21@localhost:27017/crawler-pwp21"

var testdata = JSON.parse(fs.readFileSync("json_testfile.json",  {encoding: "utf8"}))
console.log(testdata)
writeToDatabase(testdata)
function writeToDatabase(data) {
    MongoClient.connect(url, function(err, db){
        if (err) { 
          console.log("Please check your connection parameters");
        } else {
          console.log("Connection success");
          var dbo = db.db("crawler-pwp21");
          dbo.collection("test").insertMany(data, function(err, res) {
              if (err) throw err;
              console.log("Saved test file to mongodb")
              db.close();
          });
        }
      });
} 
