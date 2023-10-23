# 4chan Board Monitor

Ce programme en Python permet de surveiller les boards de 4chan en spécifiant des tags de recherche. Il scrute les threads pour les tags spécifiés, puis télécharge et stocke les threads correspondants localement dans des dossiers organisés.

## Dépendances

    Python 3.x
    requests
    BeautifulSoup4
    tqdm

Vous pouvez installer les dépendances nécessaires avec pip :

```bash
pip install requests beautifulsoup4 tqdm
```

## Utilisation

1. Clonez le dépôt :

```bash
git clone https://github.com/stek0300/4check.git
cd 4check
```

2. Exécutez le script :

```bash
python monitor.py -b [board] -t [tag1 tag2 ...] -p [chemin]
```
    -b ou --board : spécifie le board 4chan à surveiller (par exemple, b pour le board Random).
    -t ou --tag : spécifie un ou plusieurs tags à surveiller.
    -p ou --path : (optionnel) spécifie le chemin complet pour le dépôt des threads.

Par exemple, pour surveiller le board Random (b) pour des threads contenant les tags "meme" et "pepe", et stocker les résultats dans un dossier spécifié :

```bash
python monitor.py -b b -t meme pepe -p /chemin/vers/dossier
```
Le programme continuera de surveiller le board et de télécharger les threads correspondants jusqu'à ce que vous l'arrêtiez avec Ctrl+C.

## Structure de Dossier

Le programme crée une structure de dossier pour organiser les threads téléchargés :

- 📂 threads : *(Dossier principal contenant tous les threads téléchargés.)*
  - 📂 no_thread : *(Un dossier pour chaque thread, nommé avec le numéro du thread.)*
    - 📄 no_thread.txt : *(Fichier texte contenant les données du thread.)*
    - 📄 index.html : *(Fichier HTML du thread, modifié pour que les liens soient absolus.)*

## Note

Ce projet est développé par un débutant en programmation et peut contenir des dysfonctionnements. Il n'est pas prévu de mises à jour régulières pour ce code. Cependant, n'hésitez pas à le modifier, l'améliorer ou le partager comme vous le souhaitez. 
