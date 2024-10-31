# Explication SQL

## Clés primaire et clés étrangères

 •  **Clé primaire** : c'est un identifiant unique pour chaque ligne d'une table. Par exemple la colonne *id_user* dans la table *user* est une clé primaire. Elle garantit que chaque utilisateur a un id unique.
 - Exemple : 
    _________________________
   | id_user int PRIMARY KEY |
    _________________________

 • **Clés étrangères** : C'est une colonne dans une table qui fait référence a une clé primaire d'une autre table. Elle permet d'établir des relations entre différentes tables. Par exemple, dans la table *adresse*, la colonne *id_user* est une clé étrangère qui référence l'id d'un utilisateur dans la table *user*. Cela permet de dire qu'une adresse appartient à un utilisateur spécifique.
 - Exemple : 
    ________________________________________________
   | FOREIGN KEY (id_user) REFERENCES user(id_user) |
    _______________________________________________



## Relations entre les Tables
Dans une base de données, les tables ne sont pas isolées. Elles sont souvent reliées entre elles par des relations qui definissent comment les données sont connectés.

    - ***un-à-plusieurs (relation 1)***

Cette relation signifie qu'une ligne dans une table peut être reliée à plusieurs lignes dans une autre table.
- Exemple : Un utilisateur peut avoir plusieurs adresses, mais chaque adresse est associée à un seul utilisateur. C'est une relation **1 entre _user_ et _adresse_**
╰┈➤ Mise ne place : 
   ________________________________________________
  | FOREIGN KEY (id_user) REFERENCES user(id_user) |
   ________________________________________________

Cela signifie que chaque adresse est associée à un utilisateur via l'id de l'utilisateur (***id_user***), mais un utulisateur peut avoir plusieurs adresses.

    - ***plusieurs-à-plusieurs (relation N)***

Cette relation signifie que plusieurs lignes dans une table peuvent être reliées à plusieurs lignes dans une autre table. Dans ce cas, on utilise une **table de jonction** (*junction table*) pour représenter cette relation.
- Exemple : Un panier peut contenir plusieurs produits, et un même produit peut être dans plusieurs paniers. C'est une relation **N** entre ***panier*** et ***produit***
╰┈➤Mise en place avec une table de jonction : 

  ___________________________________________________________
 |CREATE TABLE panier_produit(                               |
 |   id_panier int,                                          |
 |   id_produit int,                                         |
 |   quantite int,                                           |
 |   PRIMARY KEY (id_panier, id_produit),                    |
 |   FOREIGN KEY (id_panier) REFERENCES panier(id_panier),   |
 |   FOREIGN KEY (id_produit) REFERENCES produit(id_produit) |
 |);                                                         |
  ___________________________________________________________

Ici, la table *panier_produit* est une table de jonction qui relie les tables panier et produit en utilisant leurs clés primaires respectives(*id_panier* et *id_produit*).Cela permet de gérer plusieurs produits dans un même panier et plusieurs paniers pour un même produit.

## Tables de Jonction

Une table de jonction est utilisée dans une relation N.
Pour lier deux tables. Elle contient généralement les clés étrangères des deux tables qu'elle relie, ainsi que parfois des informations supplémentaires.
- exemple : Dans notre cas, la table *panier_produit* relie les paniers aux produits, et elle contient aussi la quantité de chaque produit dans le panier.


## Types de données

- VARCHAR(x) : pour des chaînes de caractères (par exemple les noms, adresses, etc.), avec une limite de longueur spécifiée.

- INT : pour des entiers comme des identifiants (par exemple id_user).

- DECIMAL(x,y) : pour des nombres décimaux (comme le prix des produits). Le x correspond au nombre total de chiffres et le y au nombre de chiffres après la virgule.

- Exempe : prix DECIMAL(10,2) -- Prix avec deux décimales

## Cryptage des Informations Sensibles

L'énoncé spécifie que certaines informations sensibles, comme les mots de passe ou les numéros de cartes bancaires, doivent être cryptées pour des raisons de sécurité. Ce cryptage ne se fait pas directement dans le SQL, mais via des scripts côté serveur (comme en PHP) qui génèrent des valeurs hachées avant de les insérer dans la base de données.

- Exemple (en PHP) pour crypter un mot de passe : 
   ___________________________________________________________________
  | $hashed_password = password_hash($mot_de_passe, PASSWORD_BCRYPT);  |
   ___________________________________________________________________

## Standardisation des Noms de Colonnes

Standardisé les noms de colonnes pour qu'ils soient plus cohérents. Par exemple, toutes les clés primaires et étrangères suivent maintenant un format snake_case avec le préfixe id_ pour une meilleure lisibilité et organisation.

## Résumé :

- Clés primaires pour identifier chaque ligne de façon unique.
- Clés étrangères pour relier les tables entre elles (relation 1 ou N).
- Tables de jonction pour gérer les relations N(comme entre panier et produit).
- Cryptage des informations sensibles pour sécuriser les données personnelles comme les mots de passe.
- Types de données adaptés (VARCHAR, DECIMAL, etc.) pour organiser les informations efficacement
