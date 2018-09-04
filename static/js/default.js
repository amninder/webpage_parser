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

   //console.log("connected");
   sess = session;
   session.subscribe('com.example.broadcastsave', onbroadcast);
};

connection.open();

window.saveUrl = function saveUrl() {
    input = document.getElementById("url").value;
    console.log('save-url: ', input);
    connection.session.call('com.example.saveurl', [input]).then(
        function (res){
            console.log('saveurl: ', res);
            document.getElementById("demo").innerHTML = res;
        }
    );
};

window.fetchUrlFromSlug = function fetchUrlFromSlug() {
    input = document.getElementById("slug-url").value;
    console.log('fetch_url_from_slug: ', input);
    connection.session.call('com.example.getfromslug', [input]).then(
        function (res){
            document.getElementById('slug-title').innerHTML = res;
        }
    );
};

export connection = connection;
