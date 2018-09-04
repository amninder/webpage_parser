var autobahn = require('autobahn');
var sess = null;


var connection = new autobahn.Connection({
   url: "ws://127.0.0.1:8080/ws",
   realm: "realm1"
});
window.connection = connection;

function onbroadcast(args) {
      console.log("Broadcast Event:", args[0]);
}


connection.onopen = function (session) {

   console.log("connected");
   sess = session;
   session.subscribe('com.example.broadcastsave', onbroadcast);
};

connection.open();

module.exports = connection;
module.exports = autobahn
module.exports = sess
