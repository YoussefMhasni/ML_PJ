# Membres du groupe
Simoud Achour 
El Kaout Mohamed Amine 
M'hasni Youssef
Abdelmoula Oussema 

# ML_PJ
Pour la partie du choix du modèle le plus performant nous avons utlisé une grid search sur les parametres de 3 modèles qui sont :
1- SVC
2- Gradient Boosting Classifier
3- Random Forest
Nous avons aussi testé avec et sans les differente méthodes de balancing des données (smote et TomekLinks).
La fonction se base sur la métrique balanced accuracy pour le choix du modèle.


# Application:
Pour lancer l'application il faut lancer la web app avec la commande : docker-compose -f webapp/docker-compose.yml up --build --force-recreate  une celle ci executée il faut lancer le serving avec la commande : docker-compose -f serving/docker-compose.yml up --build --force-recreate  

# Monitoring: 
Pour faire fonctionner la partie monitoring il faut lancer la commande docker-compose -f reporting/docker-compose.yml up --build --force-recreate. la commande prend un peu de temps a cause du fichier ref_data qui est volumineux. Une fois la commande executée
il faut se rendre sur localhost:8082.
Pour voir le rapport d'évaluation du modéle, il faut ouvrir la partie Report puis View aprés avoir lancé evidently
