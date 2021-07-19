# l3_ia_projet_fin_annee - LocAnimal Project

**Pré-requis :**

Voir base de connaissance page 18 afin de connaitre les prérequis au bon fonctionnement des deux algorithmes.


____

***Dossier computer vision :***

J'ai prêté peu d'attention à cet algorithme : si le model du CNN avait pu être généré dans les temps, j'aurais ajouté la suppression du fond afin de cibler le premier plan et priorisé les teintes plutôt que les similitudes (les grands traits (propre à la race/espèce) étant déjà vérifié par le CNN). Cela dans l'objectif de pouvoir présenter des images similaires à un certains pourcentages à l'utilisateur. (Résultat relatif vu que computer vision pas adapté mais fonctionnel au vu du délais)

Cet algorithme n'est en aucun cas le meilleur choix mais plutôt un choix de substitution à la reconnaissance facial dans le cas du questionnement : l'animal est -il exactement le même sur les deux photos.

Si les trois mois promis avaient été accordé, l'option logique aurait pu être envisagé et combiné à un CNN fonctionnel.

__

fichier main.py    : algo comparant deux images et retournant un pourcentage


____

***Dossier CNN :***

L'algorithme présent n'a (à l'heure ou le readme a été push) pas fini de s'entrainer. Je ne peux donc pas affirmer si celui-ci est fonctionnel et entrainera bien un model pertinent ou si sa construction est erronée.

Les réglages de ces algos sont ceux d'un dataframe plus volumineux (réglages test), mais pour des raisons de volume, une bdd d'images plus légère a été push.

L'objectif de cet algorithme est de générer un model visant à pouvoir identifier l'espèce, la race et la couleur de l'animal présent sur une photo. Cet algorithme servira en parallèle à un pré-tri pour l'algo de comparaison d'image.

__


fichier _download.py    : télécharge des images

fichier _params.py      : parametre pour le téléchargement des images et le cnn

fichier training.ipynb  : cnn
