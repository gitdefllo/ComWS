################
# XML-RPC Client
################
import xmlrpclib
import msvcrt as msvcrt

# constantes de l'adresse serveur
host = 'localhost'
port = 9090

# obtenir le nombre de fin de la suite de Fibonacci
def getRange():
	index = 15
	print 'Selectionnez un nombre:'
	# essaye de caster l'input de l'utilisateur en integer
	try:
		# retourne la valeur entree
		index = int(msvcrt.getch())
	# si echec, on reitere la demande d'input
	except ValueError:
		print 'Ce n\'est pas un nombre valide. Veuillez reessayer...\n'
		# rappel recursif de la methode
		getRange()
		return

	return index

def main():
	# connexion au serveur
    url = "http://{}:{}".format(host, port)
    proxy = xmlrpclib.ServerProxy(url)
    print 'Requests sent to {} at port {} ...'.format(host, port)

    # demande d'input a l'utilisateur
    endrange = getRange()
    # appel de la fonction en xml-rpc
    fibonacci = proxy.Fibonacci(endrange)
    # affiche la reponse obtenue
    print 'Fibonacci answer: {}'.format(fibonacci)

# execution du programme
if __name__ == '__main__':
    main()