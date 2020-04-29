### Rendre facilement les *jupyter notebook .ipynb* exécutables par les visiteurs

* créer les *.ipynb* sur son propre serveur *jupyter notebook* local, ou en ligne avec *colaboratory*.

* fichiers *.ipynb* obligatoirement dans un dépôt gitlab, github. Pas de dépôt sur site perso! 

* URL du dépôt *Clone with HTTPS* à insérer dans [myblinder.org](myblinder.org), un serveur jupyter notebook en ligne, où il est possible d'avoir également ce lien [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/fgachelin/physique-python.git/master) à insérer où on le souhaite.

### Choix de github


* *Gitlab*, *Framagit* n'affichent pas correctement le latex du markdown.


* *Colaboratory* nécessite un compte google, et l'export *.pdf* est impossible.


* Rendu Latex seulement sur *.ipynb*, ne fonctionne pas dans fichier *.md*. Par exemple $E=mc^2$...


### Important


* *apt.txt* contient ce que debian local du serveur doit installer, notament *texlive* pour la création des *.pdf*.


* *requirements.txt*, absent ici, contiendrait les modules python à installer par *pip*.
