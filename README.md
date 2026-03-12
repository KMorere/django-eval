# Evaluation Web Python - Échange de compétence :

# Sommaire
- [Introduction](#introduction)
- [Installation](#installation)
- [Architecture](#architecture)

# Introduction
Il s'agit de spécifier, concevoir et réaliser le prototype d'un système qui permettrait à des 
personnes d'échanger des compétences (ex. : jardinage, administration d'un ordinateur), 
permettant d'accomplir des activités (ex. : tailler un rosier, installer un logiciel), avec des 
personnes près d'elles, à des créneaux leur convenant, et en tenant compte de la météo si 
certaines activités en dépendent. 

Ce prototype est une application Web, qui n’intégrera pas – dans cette première version 
demandée pour cette évaluation – la recherche de proximité des personnes, ni l’utilisation de 
la météo pour savoir si un créneau est favorable à une activité et considérera qu’un créneau 
est une journée entière (à l’intérieur de laquelle on suppose que les personnes peuvent 
convenir d’un créneau pour se rencontrer). 

# Installation
Utilisation de la version 3.14 de Python ainsi que Django 5.2.12.
Les packages sont également fournits dans le fichier "Requirements.txt".

## Architecture
1. Home :
Le site affiche les requêtes et activités futures sur la page principale,
Si un utilisateur est connecté il pourra accepter une requête d'un autre utilisateur.

2. Skills :
Page servant à afficher toutes les compétences séparées par catégories.

3. Requests :
Formulaire de création d'une requête à partir d'un jour de disponibilité et une tache.

4. Profile :
Page d'information de l'historique d'activité de l'utilisateur connecté et la modification de ses compétences.

-----
