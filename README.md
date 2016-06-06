###############
	README
###############

---------------------------------------
I. SOAP Serveur (rf. Badreddine Dlaila)
---------------------------------------
	Source:
	--------
		- Nom 		 	= server.js
		- Emplacement 	= ~/server/weather/

	Infos: 
	------
		- DNS 									= 'nodejsauth.azurewebsites.net'
		- Route									= '/authenticate'
		- Serveur 								= NodeJS
		- Plateforme 							= Azure
		- Base de données 						= MSQLServer 2016
		- Utilisateur par défaut (en statique) 	= 'User1','123'

	Instructions:
	-------------
		- Badreddine se connecte sur ce serveur mis à disposition sur la plateforme Azure

---------------
II. SOAP Client
---------------
	Source:
	--------
		- Nom 		 	= client.py
		- Emplacement 	= ~/webservice/weather/

	Infos: 
	------
		- DNS 					= 'authorizationservice.azurewebsites.net'
		- Route					= '/oauth2/token'
		- Client 				= Python
		- Utilisateur (défaut)  = 'badreddine.dlaila@gfi.fr','P@ssword123!'

	Instructions:
	-------------
		- Le client s'authentifie sur le serveur 
			en .Net mis à disposition par Badreddine
		- Puis, il exécute ensuite les scripts de 
			'weather.py' pour appeler le service externe

------------------------------
III. XML-RPC Serveur / Client:
------------------------------
	Sources:
	--------
		- Nom 		 	= server.py 		& client.py
		- Emplacement 	= ~/server/rpc/ 	& ~/webservice/xmlrpc/

	Infos: 
	------
		- Serveur 								= Python
		- Client 								= Python
		- Base de données 						= Aucune
		- Utilisateur par défaut				= Aucun

	Instructions:
	-------------
		- En local, démarrer le serveur en entrant: 
			'python ~/rpc/server.py'
		- Ensuite, démarrer le client en entrant dans une autre fenêtre: 
			'python ~/services/xmlrpc/client.py'