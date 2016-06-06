// import des modules requis
var mongoose = require('mongoose');
var Schema = mongoose.Schema;

// creation du modele User
var userSchema = new mongoose.Schema({
    pseudo: { 
    	type: String, 
    	required: true, 
    	unique: true 
    },
    email:  { 
    	type: String, 
    	required: true, 
    	unique: true 
    },
    password: { 
    	type: String, 
    	required: true 
    }, 
    admin: {
        type: Boolean,
        default: false
    }
});

// export du modele
module.exports = mongoose.model('User', userSchema);