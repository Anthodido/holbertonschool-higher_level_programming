BASIC of HTTP/HTTPS
___

HTTP et HTTPS sont des protocoles client-serveur basé sur des messages, requetes - réponse.
En revanche HTTPS est une version amélioré de HTTPS car les messages qu'il transmets sont
crypté en SSL/TLS et donc plus sécurisés.

___

SCHEMA démonstratif : Echange HTTP

```
+---------+ +-----------+ +-----------+ +----------+
| Client | -----> | Web layer | -----> | API layer | -----> | Database |
| (app) | <----- | (proxy) | <----- | (logic) | <----- | (data) |
+---------+ +-----------+ +-----------+ +----------+
Request: method + URL + headers + body
Response: status + headers + body (souvent JSON)

````

___

Code/Methode http courant

| Méthode | Intention                     | Notes importantes                            |
|---------|-------------------------------|----------------------------------------------|
| GET     | Lire une ressource            | Sans effet côté serveur (idempotent).        |
| POST    | Créer / déclencher une action | Non-idempotent par défaut.                   |
| PUT     | Remplacer une ressource       | Idempotent ; envoie l'objet complet.         |
| PATCH   | Modifier partiellement        | Idempotent souvent, selon implémentation.    |
| DELETE  | Supprimer                     | Idempotent en pratique (suppression répétée).|
------------------------------------------------------------------------------------------
