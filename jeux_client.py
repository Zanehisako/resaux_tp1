import socket
ConnexionAUnServeur = socket.socket() # Creation de socket

host = "127.0.0.1" # adresse de la machine distante
port = 900# numero de port

ConnexionAUnServeur.connect((host,port))

message_A_Transmettre=""
message_recu = ""
while True:
    message_recu = ConnexionAUnServeur.recv(1024).decode('ascii')
    print(message_recu)
    if "#YOUWON" in message_recu:
       ConnexionAUnServeur.close() # cloture de la connexion avec le serveur (envoie flag FIN) 
       break 
    message_A_Transmettre=input() # lecture depuis le clavier
    message_A_Transmettre += "#TRY"
    ConnexionAUnServeur.send(message_A_Transmettre.encode('ascii')) # transmettre le message vers le serveur

ConnexionAUnServeur.close() # cloture de la connexion avec le serveur (envoie flag FIN) 
print( "Fin du programme")
