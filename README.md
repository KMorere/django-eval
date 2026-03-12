# Evaluation Web Python - Échange de compétence :

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

-----

[optionnel] Les compétences pourront être regroupés en catégories. 
Il est demandé d'écrire une application Web Django permettant : 

• à tout internaute « visiteur » d’afficher par exemple :  
- les prochains créneaux où un utilisateur a proposé d’apporter son aide – à travers une 
  de ses compétences – à un autre utilisateur pour une activité (affichage anonyme où les 
  utilisateurs impliqués ne sont pas mentionnés),  
- la liste des compétences que l’application propose à ses utilisateurs d’échanger;  

• à un « utilisateur » connecté U1 :  
• d’indiquer :  
- parmi la liste des compétences, celles qu'il possède et est prêt à offrir,  
- [optionnel] les créneaux où il est disponible pour les mettre en œuvre pour aider un 
autre utilisateur qui aurait besoin d’une de ses compétences,  
- les créneaux où il recherche quelqu’un pour l’aider dans une activité (qu’il précise 
sous une forme libre) où il n’a pas la compétence correspondante (qu’il sélectionne 
dans la liste des compétences qu’il ne possède pas);  
• d’afficher les prochains créneaux1 où un autre utilisateur U2 recherche quelqu’un pour 
l’aider dans une activité où il n’a pas la compétence correspondante (en n’affichant que 
les créneaux pour lesquels l’utilisateur U1 a indiqué posséder la compétence
recherchée); 
il peut alors indiquer qu’il désire se rendre disponible pour ce créneau, 
lequel ne sera alors plus proposé à aucun utilisateur dans cet affichage,  
- [optionnel] d’afficher les prochains créneaux où un autre utilisateur a indiqué se rendre 
disponible pour l’aider dans une activité où il ne possède pas la compétence 
correspondante.  
- [optionnel] seulement les créneaux où il a indiqué être lui-même disponible. 
Il est à préciser que les informations visibles par un utilisateur connecté au sujet d’un autre 
utilisateur sont le prénom, le nom et l’adresse de courriel (cette dernière permettant aux deux 
utilisateurs concernés par un créneau d’aide de se contacter pour convenir des modalités de 
leur rencontre).
 
L’ensemble des compétences, ainsi que les utilisateurs autorisés à se connecter pourra être 
entré en dur par le site d’administration de Django.  
