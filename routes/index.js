// import des modules requis
var express 	= require('express');
var router 		= express.Router();
var mongoose  = require('mongoose');
var colors 		= require('colors');
var jwt    		= require('jsonwebtoken');

// constantes des modeles et configuration des routes
var User   = require('../models/user');
var config = require('../config');

// route par défaut du serveur
router.get('/', function (req, res) {
	console.log('GET / called'.yellow);
	res.end('Welcome to Authenticate Server (NodeJS)');
})

// methode d'authentification d'un utilisateur
router.post('/authenticate', function (req, res) {
	console.log("POST /authenticate called".yellow);
  // recherche parmi la bdd mongo avec le modele User
	User.findOne({ 
    $or: [
      { pseudo: req.body.login },
      { email: req.body.login }
    ]
  }, function (err, user) {
      // callback de la reponse
      if (err) throw err;

      if (!user) {
        console.log("User not found.".red);
        res.json({ success: false, response: "Authentication failed. User not found." });
        return;
      }

      if (user.password != req.body.password) {
        console.log("Invalid password.".red);
        res.json({ success: false, response: "Authentication failed. Invalid password" });
        return;
      }

      // creation d'un token jwt
      var token = jwt.sign(user, config.secret, {
        algorithm: 'HS256', 
        expiresIn: "24h"
      });

      console.log("Successful authentication.".green);
      console.log("...");
      res.json({ success: true, token: token });
    });
})

// methode de recuperation d'un utilisateur specifique
router.get('/user/:id', function (req, res) {
  console.log("GET /user/:id called".yellow);
  // recherche parmi la bdd mongo avec le modele User
  User.findOne({ 
    _id: req.params.id 
  }, function (err, user) {
      // callback de la reponse
    if (err) throw err;

    if (!user) {
      res.json({ success: false, response: "Not found" });
      return;
    }

    res.json({ success: true, response: user});
  });
})

// methode de recuperation de tous les utilisateur de la bdd
router.get('/users', function (req, res) {
  console.log("GET /users called".yellow);
  // recherche parmi la bdd mongo avec le modele User
  User.find({}, function (err, users) {
    // callback de la reponse
    if (err) throw err;

    if (!users) {
      res.json({ success: false, response: "No entries" });
      return;
    }

    res.json({ success: true, response: users });
  });
})

// ajoute un utilisateur dans la bdd
router.post('/user', function (req, res) {
  console.log("POST /user called".yellow);
  // creation du nouveau User
  var usertest = new User ({ 
    pseudo: req.body.pseudo, 
    email: req.body.email,
    password: req.body.password,
    admin: (req.body.admin != null ? req.body.admin : false)
  });

  // insert en bdd le nouvel User
  usertest.save(function (err) {
    if (err) throw err;

    res.json({ success: true, response: "New user saved successfuly." });
  });
});

// export des routes
module.exports = router;