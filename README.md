# **Python Joke App**

# ue19-lab-05

Cette application Python interroge une API publique (JokesAPI) pour afficher une blague aléatoire. Elle est contenue dans un environnement Docker pour simplifier son exécution.

## Prérequis

- Python 3.x
- Bibliothèque `requests`

Vous pouvez installer la bibliothèque `requests` en utilisant pip :

```bash
pip install requests

```
## **Installation et utilisation**

### **1. Cloner le repository**
Téléchargez le code source en clonant ce repository :
```
git clone https://github.com/<votre_nom_utilisateur>/ue19-lab-05.git
cd ue19-lab-05
```

## Fonctionnalités
- Récupère une blague aléatoire en français depuis l'API JokeAPI.
- Affiche la blague dans la console.
- Gère les blagues en deux parties (setup et delivery) ainsi que les blagues en une seule partie.
- Affiche un message d'erreur si l'API ne répond pas correctement.

## Exemple de sortie

```
 Pourquoi les programmeurs préfèrent-ils le noir ? Parce que c'est la couleur par défaut !
```
