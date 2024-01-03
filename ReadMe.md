## Docker commands
- docker container prune && docker volume prune 
- docker compose up --build 

## Utilisateurs
admin : 
- username: root
- password: root

users :
- username: client2
- password: clipass2

## Api
### Connexion 
- Récupération du token : Call api post sur api-token-auth/ avec username et password
- Ajout du token dans le header 'Authentication: Bearer token_value'

### Endpoints
- Incendie : api/fire
- Capteur : api/sensor/
- Relevé capteur : api/reading/