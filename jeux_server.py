mport random time
from socket import socket
= ( ). (). ( )List_mots open "dictionnaire.txt" read split "\n"
= ()socket_serveur socket
. (( , ))socket_serveur bind "localhost" 900
. ( )socket_serveur listen 10
:while True
, = . ()connexion _ socket_serveur accept
= . ()start time time
= [ ( . () ( ))]mot_aleatoire List_mots int random random *len List_mots
= ( )lettres list mot_aleatoire
. ( )random shuffle lettres
. (( . ( ) ). ( ))connexion send "" join lettres +"#GAMESTART\r\n" encode "ascii"
=guess ""
:while "#FINISH\r\n" not in guess
=guess ""
:while True
+= . ( ). ( )guess connexion recv 1024 decode "ascii"
:if "#TRY\r\n" in guess break
= . ( )[ ]guess guess split "#" 0
. ()== . ():if guess lower mot_aleatoire lower
. (( ( . () ) ). ( ))connexion send "#YOUWON "+str time time -start +"\r\n" encode "ascii"
. ( )connexion send b"#WRONG\r\n"
. ()connexion clos
