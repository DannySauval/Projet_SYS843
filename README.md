# Projet_SYS843

Avec l'avènement des nouvelles technologies, la société actuelle cherche de plus en plus à automatiser les tâches effectuées par l'être humain. Les robots dans le domaine industriel permettent de remplacer les opérateurs qui faisaient des tâches dangereuses ou bien pénibles. De même dans le domaine automobile, des entreprises comme \textit{Google} ou \textit{Uber} développent des systèmes de pilotage automatique. Cependant, comment un tel système peut-il être capable d'analyser un environnement afin de pouvoir répondre instantanément à un environnement changeant et toujours différent ? Les êtres humains sont capables de faire cela simplement, mais les machines doivent être dotées d'un grand nombre de capteurs ainsi que d'un système de traitement des données très complexe afin de prendre les bonnes décisions. L'un des principaux fondements d'un système de pilotage automatique est la vision. Une voiture autonome doit être capable de "voir" son environnement et ensuite d'analyser celui-ci afin de détecter les objets pour les éviter et la route pour la suivre. Ce papier présente l'étude expérimentale qui a été effectuée afin de mettre en place un système de détection d'objets. Ce système est basé sur Faster R-CNN que j'ai pu présenter dans ma synthèse de littérature. La section suivante (\autoref{sec:somm}) présente un rappel du principe de Faster R-CNN.

## Fichiers
Les fichiers de ce Github permettent de traiter la base de données PascalVOC 2012. Ils peuvent cependant simplement être adapté à n'importe quelle database contenant des images et annotations.

## Configuration
Le projet a été entièrement mené sur un Laptop Lenovo Legion Y520, i5-7300HQ 2.5 GHz (boost 3.5 GHz), 8 GB RAM, NVidia GeForce GTX 1060 6GB MaxQ-Design. Le système d'exploitation utilisé est Windows 10 version 1809.
L'IDE utilisé pour ce projet est PyCharm. C'est selon moi un des meilleurs IDE pour Python qui permet de ne pas trop se compliquer la vie avec l'installation de librairies.
Afin de pouvoir exécuter les fichiers du projet, il est nécessaire d'installer les librairies suivantes : 

tensorflow, tensorflow-gpu : Très important, sans cela le GPU n'est pas utilisé et l'entraînement est beaucoup trop long, Keras, Pillow, numpy, opencv-python, opencv-contrib-python, pandas, scikit-learn, scikit-image, scipy et sklearn.

## Documentation
Le fichier Projet_RDN.pdf présente le projet ainsi que les résultats que j'ai obtenu.

## Remerciement

Je souhaite remercier Ismail Ben Ayed, chargé du cours SYS843 à l'ETS pour m'avoir enseigné et fait comprendre beaucoup de techniques de machine learning. Ces connaissances acquises m'ont permis de traiter au mieux le problème de mon projet et ont été de très bonnes pistes pour développer mon savoir.
