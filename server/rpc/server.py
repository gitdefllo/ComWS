################
# XML-RPC Server
################
from SimpleXMLRPCServer import SimpleXMLRPCServer
import inspect

# constantes de l'adresse serveur
host = 'localhost'
port = 9090

# classe des methodes disponibles du serveur
class Methods(object):
    # execution et retour de la suite de Fibonacci de 0 a {n}
    def Fibonacci(self, n):
        fibo = range(0, n)
        fibo[0] = 1
        for i in fibo[2 : n]:
            fibo[i] = fibo[i - 1] + fibo[i - 2]
        
        return fibo

def main():
    # creation du serveur en xml-rpc
    server = SimpleXMLRPCServer((host, port))
    print "Listening on {} at port {} ...".format(host, port)

    # recuperation des methodes existantes
    methods = Methods()
    # recuperation de la methode Fibonacci( {n} )
    fibonacci = methods.Fibonacci
    # enregistrement de la methode sur le serveur
    server.register_function(fibonacci, 'Fibonacci')
    # faire tourner le serveur indefiniment
    server.serve_forever()

# execution du programme
if __name__ == '__main__':
    main()