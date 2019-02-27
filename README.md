TP qui consiste a developper un modele vectoriel de recherche d'information sur la base de la representation VSM.  

La hierarchie du repertoire est la suivante  

|--antiDict/  
|--clean/  
|--json/  
|--split/  
|--src/  
&nbsp; |--split_cacm.py  
   |--tokenize_cacm.py  
   |--courbe.py  
   ...  
|--cacm.all  
|--common_words  
...  

L'ordre d'execution est le suivant (avec une explication de la fonction du programme):  

1 - split_cacm.py  
  Pour chaque balise .I, la fonction suivante extrait les contenu des balises .T, .A, .W et .B 
  en les mettant dans un fichier portant le nom CACM-XX où XX est le numero associe a la balise .I 

2 - tokenize_cacm.py  
  La fonction Numberless ouvre un a un les fichiers CACM-XX du repertoire split (rempli a l'etape precedente), 
  et pour chaque fichier, ne garde que des mots qui commencent par une lettre et qui 
  ne contiennnent que des lettres et des chiffres et ecrit le resultat (en minuscule) 
  dans un autre fichier portant le meme nom et avec l'extension .flt en plus.  

3 - courbe.py  
  calcul de la frequence d'apparition de tous les termes de la collection et
  tri par le nombre d'apparition decroissant afin d'afficher
     a) Les 10 termes les plus frequents dans l'ordre decroissant avec leur nombre d'occurrences
     b) La taille du vocabulaire
     c) La valeur lambda theorique calculee.
     d) La courbe qui present le nombre total d'occurrences en fonction du rang de tous les termes.
     e) La courbe de Zipf theorique pour les rangs de 1 au nombre de termes du vocabulaire.

4 - anti-dict.py  
  Fonction qui applique l'anti-dictionnaire (fichier common-words)
  sur les mots en minuscule en enlevant tous les termes de ces fichiers qui y apparaissent. 
  Le resultat du filtrage est mis dans un fichier portant le meme nom que ces fichiers avec 
  une nouvelle extension .sttr 

5 - vocabjson.py  
  Construction du vocabulaire associe a la collection .sttr en considerant tous les termes
  qui apparaissent au moins une fois. Le resultat est stocke dans un fichier “vocabulaire.json”
  format terme: document_frequency

6 - vect.py  
  construction de la representation vectorielle de tous les documents d'apres le modele vectoriel de Salton.
  Le type de representation choisi est une representation creuse (sparse) de chaque document d 
  avec un dictionnaire de couples (terme, tf.idf du terme dans d), ou idf_i = ln(N/df_i) 
  On ne se preoccupe pas encore de la normalisation.

7 - IndexInverse.py  
  Construction de l'indexe inverse a partir de la representation vectorielle des documents.
  Resultat dans le fichier indexInverse.json en format terme: {idDoc: tf.idf dans le doc}

8 - norme.py  
  calcul de le norme de chaque document

9 - recherche.py  
  Recuperation et traitment des requetes en calculant la correspondace RSV par un cosinus