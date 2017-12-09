var MongoClient = require('mongodb').MongoClient;
var assert = require('assert');
var ObjectId = require('mongodb').ObjectID;
var url = 'mongodb://localhost/tweets';



// find total number of tweets
var findTweets = function(db,callback) {
  var totalTweet=0;
MongoClient.connect('mongodb://localhost/tweets', function(err, db) {
  assert.equal(null, err);
  db.collection('narendra_modi').find({}).count()
    .then(function(numItems) {
      totalTweet=totalTweet+numItems; 
    })
});
MongoClient.connect('mongodb://localhost/tweets', function(err, db) {
  assert.equal(null, err);
  db.collection('kejriwal').find({}).count()
    .then(function(numItems) {
      totalTweet=totalTweet+numItems;
    })
});
console.log("mahika"+totalTweet);
};

// find number of retweets
var findRetweets = function(db, callback) {
  var totalRetweets=0;
   var namo =db.collection('narendra_modi').find( ); 
   var kejri =db.collection('kejriwal').find( );

   
   namo.each(function(err, doc) {
      assert.equal(err, null);
      if (doc != null) {
         totalRetweets=totalRetweets+doc.retweet_count;
      } else {
         callback();
      }
   });

   kejri.each(function(err, doc) {
      assert.equal(err, null);
      if (doc != null) {
         totalRetweets=totalRetweets+doc.retweet_count;
      } else {
         callback();
      }
   });
   console.log("mahikawason"+totalRetweets);

};

//find number of favourite count
var findfavourite = function(db, callback) {
  var totalFavourite=0;
   var namo =db.collection('narendra_modi').find( ); 
   var kejri =db.collection('kejriwal').find( );

   
   namo.each(function(err, doc) {
      assert.equal(err, null);
      if (doc != null) {
         totalFavourite=totalFavourite+doc.favorite_count;
      } else {
         callback();
      }
   });

   kejri.each(function(err, doc) {
      assert.equal(err, null);
      if (doc != null) {
         totalFavourite=totalFavourite+doc.favorite_count;
      } else {
         callback();
      }
   });
   console.log("mahikawason"+totalFavourite);

};





MongoClient.connect(url, function(err, db) {
  assert.equal(null, err);
  findTweets(db,function() {
    db.close();
  });


  findRetweets(db,function() {
    db.close();
  });

findfavourite(db,function() {
    db.close();
  });

  // returnTweets(db, function() {
  //   db.close();
  // });
  
});
