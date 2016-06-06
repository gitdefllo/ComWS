###############
	README
###############

-------------------------
I. SOAP Serveur / Client:
-------------------------
	Infos: 
	------
		- Serveur 								= NodeJS
		- Client 								= Python
		- Base de données 						= Mongo Labs
		- Utilisateur par défaut (en statique) 	= 'User1 / 123'

	Instructions:
	-------------
		- En local, démarrer le serveur en entrant: 
			'node ~\weather\server.js'
		- Ensuite, démarrer le client en entrant dans une autre fenêtre: 
			'python ~\services\weather\client.py'

-----------------------------
II. XML-RPC Serveur / Client:
-----------------------------
	Infos: 
	------
		- Serveur 								= Python
		- Client 								= Python
		- Base de données 						= Aucune
		- Utilisateur par défaut				= Aucun

	Instructions:
	-------------
		- En local, démarrer le serveur en entrant: 
			'python ~\rpc\server.py'
		- Ensuite, démarrer le client en entrant dans une autre fenêtre: 
			'python ~\services\xmlrpc\client.py'