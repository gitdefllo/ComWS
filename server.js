// import des modules requis
var express 	= require('express');
var app 		= express();
var colors 		= require('colors');
var mongoose 	= require('mongoose');
var bodyparser  = require('body-parser');
var routes 		= require('./routes/index');
var config 		= require('./config');

// constantes du serveur
var host = 'nodejsauth.azurewebsites.net';
var port = process.env.PORT || 1337;

// prepare la connexion a la bdd
try {
	mongoose.connect(config.database);
	app.set('s3cr3t', config.secret);
} catch(e) {
	console.log(e.red);
}

// connexion a la bdd
var db = mongoose.connection;
// si aucune connexion afficher un message d'erreur
db.on('error', console.error.bind(console, 'Connection error: '));
// si la connexion reussi, afficher un message de reussite
db.once('open', function() { console.log("Database opened".yellow) });
	
// preparation du parsing json pour les appels/envois des methodes du serveur
app.use(bodyparser.urlencoded({ extended: false }));
app.use(bodyparser.json());
// utilisation des routes definies du serveur
app.use('/', routes);

// creation du serveur et mise en marche
var server = app.listen(port, host, function (req, res) {
  	console.log("\nServer listening at http://%s:%s".green, host, port);
  	console.log("...");
  	
  	res.writeHead(200, { 'Content-Type': 'text/plain' });
  	res.end('Hello from azure\n');
})

// export de l'application
module.exports = app;