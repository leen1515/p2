# Préparez des données pour un organisme de santé publique

## Introduction
Ce projet établit la faisabilité d'une application destinée à améliorer la qualité des informations sur les nouveaux produits alimentaires ajoutés manuellement par les utilisateurs. L'application automatisera les suggestions de valeurs d'entrée pour réduire les erreurs et combler les lacunes dans les données saisies manuellement. Elle utilise des algorithmes, des statistiques pour fiabiliser les nouvelles entrées de données alimentaires.

## Objectifs de l'application
- Automatiser les suggestions de valeurs d'entrée pour les nouveaux produits.
- Améliorer la précision et la complétude des données dans la base de données.
- Faciliter l'intégration et l'analyse des données nutritionnelles par les utilisateurs.

## Dépendances
Ce projet nécessite les bibliothèques Python suivantes :

numpy==1.26.4
pandas==2.2.2
matplotlib==3.8.4
seaborn==0.13.2
scikit-learn==1.4.1.post1
plotly==5.21.0
jupyterlab



Évaluation de la faisabilité basée sur les résultats des analyses.

## Utilisation 

L'environnement et le notebook sont containerisés dans une image docker.
Voici le lien et les indications pour l'executer.
```
docker pull ghcr.io/leen1515/p2:latest
```
Verifier l'image:

```
docker images
```
Préparer un repertoire
```
cd nouveau_dossier
```
Lance le container
```
docker run -p 8888:8888 -v ${PWD}:/home/jovyan/work --name p2 ghcr.io/leen1515/p2:latest
```

Accèder au container
http://127.0.0.1:8888/lab