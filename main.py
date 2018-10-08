#Données extraite d'une : Etude du profil de la méthylation de l'ADN des cellules mononucléées du sang périphérique chez des personnes âgées sédentaires, sportives et des jeunes sédentaires. 

#Data extracted: Study of the DNA methylation profile of peripheral blood mononuclear cells (PBMC) in sedentary, sporty and sedentary elderly people.

#Ouverture du référentiel illumina 450k
#Open the 450k illumina repository

class Read():
  def __init__(self, fichier):
    self.fichier = fichier
    
  def lecture(self):
    import csv
    dataa =[]
    f = open(self.fichier, "r")
    f_csv = csv.reader(f,delimiter=" ")
    data = list(f_csv)
    data = data[38:]
    for d in data:
      for d1 in d:
        r = d1.split("\t")
        dataa.append(r)
    return dataa

  def liste_new (self, regex):
    dic ={}
    import re
    da= self.lecture()
    for d in da:
      if d[21] =='':
        d[21]= d[0]
      for r in regex:
        if re.search(r, d[21]) :
          d[21] = d[21].replace('"','')
          d[21] = d[21].split(";")
          d[21]= d[21].pop()
          d[21]="".join(d[21])
    
      if d[21] in dic:
        dic[d[21]]+="_"+d[0]
      else:
        dic[d[21]]= d[0]
    
    for k,v in dic.items():
      dic[k]= v.split("_")
    return dic
  
#Ouverture sélective des dossiers des patients par la 1ère lettre grâce à la fonction glob.glob().

#Selective opening of patients' files by the first letter thanks to the function glob.glob ().

class Representation_genetique():
  def __init__(self, groupe):
    self.groupe = groupe
    import os
    import glob
    self.liste_fichier =[]
    chemin = os.getcwd()
    for g in self.groupe: 
      liste = glob.glob(chemin+"/"+"["+g+"]"+"*.txt")
      self.liste_fichier.append(liste)

#Transformation des données des patients sélectionnés  en dictionnaire en fonction du referentiel illumina.

#Transformation of the data of the selected patients into a dictionary according to the illumina referential.

  def dictionnaire_genetique(self, dico_r):
    import csv
    data1 =  []
    dico ={}
    for fic in self.liste_fichier:
      for fichier in fic:
        f = open(fichier, "r")
        f_csv = csv.reader(f,delimiter=" ")
        data = list(f_csv)
        data = data[4:]

        for d in data:
          for d1 in d:
            r = d1.split("\t")
            data1.append(r)
    
    for k,v in dico_r.items():
      for da in data1:
        if da[0] in dico_r[k]:
          if k in dico:
            dico[k]+= "_"+da[1]
          else:
            dico[k]= da[1]
    
    return dico

#Présentation sous forme de tableau
#Presentation in tabular form

  def tableau(self, dictionnaire):
    import pandas
    for k, v in dictionnaire.items():
      dictionnaire[k]=  pandas.Series(v.split("_"), dtype = float )
    array = pandas.DataFrame(dictionnaire)
    array = array.fillna(0)
    return array

   

class Categorie_phenotypique():
  def __init__(self, t1,t2,t3):
    self.t1=t1
    self.t2=t2
    self.t3=t3
    

  def table_concatener(self, n1,n2,n3):
    import pandas
    array_final = pandas.concat([self.t1.rename(n1),self.t2.rename(n2),self.t3.rename(n3)],axis =1, sort =True)
    return array_final
  
  



class Categorie_phenotypique2():
  def __init__(self, t1,t2,t3,t4,t5,t6):
    self.t1=t1
    self.t2=t2
    self.t3=t3
    self.t4=t4
    self.t5=t5
    self.t6=t6
    

  def table_concatener2(self, n1,n2,n3,n4,n5,n6):
    import pandas
    array_final = pandas.concat([self.t1.rename(n1),self.t2.rename(n2),self.t3.rename(n3),self.t4.rename(n4),self.t5.rename(n5),self.t6.rename(n6)],axis =1, sort =True)
    return array_final

#Présentation des données sous forme de graphe (boîte à moustache).

#Presentation of the data as a graph (boxplot).

class Graphique():
  def __init__(self, array):
    self.array = array
    
  def boxplot(self, title, label_y):
    import matplotlib.pyplot as plt
    plt.boxplot([self.array[k] for k in self.array.keys()], labels = self.array.keys())
    plt.title(title,fontsize= 6.6,fontname="serif",color="royalblue", fontstyle ="italic", weight = "heavy")
    plt.xticks(fontsize=6,fontname="serif",weight = "bold", rotation = 7.5, color = "green")
    plt.ylabel(label_y, fontsize=6.9,fontname="serif")
    return plt.savefig('graph1.png')

  def boxplot2(self, title, label_y):
    import matplotlib.pyplot as plt
    plt.boxplot([self.array[k] for k in self.array.keys()], labels = self.array.keys())
    plt.title(title,fontsize= 6.6,fontname="serif",color="royalblue", fontstyle ="italic", weight = "heavy")
    plt.xticks(fontsize=5.5,fontname="serif",rotation = 17, color ="green", weight = "bold")
    plt.ylabel(label_y, fontsize=6.9,fontname="serif")
    return plt.savefig('graph2.png')
    

#Création de l'instance:
#Instance creation:

referentiel = Read("referentiel.txt")

#Application des méthodes:
#Application methods:

liste_referentiel = referentiel.liste_new(['"MAEL;MAEL"','"PINK1;PINK1"'])

print(liste_referentiel)

#Création des instances:
#Creating instances:

#Instances par âges et mode de vie (sédentaire ou sportif):

#Instances by age and lifestyle (sedentary or athletic):

agees_sedentaires = Representation_genetique(["f","h"])
jeunes_sedentaires =  Representation_genetique(["j","y"]) 
agees_sportives = Representation_genetique(["m","w"]) 

#Instances par sexe, âge et par le mode de vie (sédentaire ou sportif) 

#Instances by sex, age and lifestyle (sedentary or athletic)

femmes_agees_sedentaires = Representation_genetique(["f"])

hommes_ages_sedentaires = Representation_genetique(["h"])

femmes_jeunes_sedentaires = Representation_genetique(["y"])

hommes_jeunes_sedentaires = Representation_genetique(["j"])

femmes_agees_sportives = Representation_genetique(["w"])

hommes_ages_sportifs = Representation_genetique(["m"])


#Application des méthodes:
#Application methods:

#Dictionnaire du niveau méthylation par âge et par le mode de vie (sédentaire ou sportif)

#Dictionary of the methylation level by age and lifestyle (sedentary or sporty)

dico_agees_sedentaires= agees_sedentaires.dictionnaire_genetique(liste_referentiel)

dico_jeunes_sedentaires = jeunes_sedentaires.dictionnaire_genetique(liste_referentiel)

dico_agees_sportives = agees_sportives.dictionnaire_genetique(liste_referentiel)

#Dictionnaire du niveau méthylation par âge, sexe et par le mode de vie (sédentaire ou sportif)

#Dictionary of the methylation level by age, sex and lifestyle (sedentary or sporty)

dico_femmes_agees_sedentaires= femmes_agees_sedentaires.dictionnaire_genetique(liste_referentiel)

dico_hommes_ages_sedentaires= hommes_ages_sedentaires.dictionnaire_genetique(liste_referentiel)

dico_femmes_jeunes_sedentaires= femmes_jeunes_sedentaires.dictionnaire_genetique(liste_referentiel)

dico_hommes_jeunes_sedentaires= hommes_jeunes_sedentaires.dictionnaire_genetique(liste_referentiel)

dico_femmes_agees_sportives= femmes_agees_sportives.dictionnaire_genetique(liste_referentiel)

dico_hommes_ages_sportifs= hommes_ages_sportifs.dictionnaire_genetique(liste_referentiel)

#Tableau du niveau méthylation par âge et par le mode de vie (sédentaire ou sportif)

#Table of the level methylation by age and lifestyle (sedentary or athletic)

tableau_agees_sedentaires = agees_sedentaires.tableau(dico_agees_sedentaires)

tableau_jeunes_sedentaires=jeunes_sedentaires.tableau(dico_jeunes_sedentaires)

tableau_agees_sportives= agees_sportives.tableau(dico_agees_sportives)


#Tableau du niveau méthylation par âge, sexe et par le mode de vie (sédentaire ou sportif).

#Table of the methylation level by age, sex and lifestyle (sedentary or athletic).

tableau_femmes_agees_sedentaires = femmes_agees_sedentaires.tableau(dico_femmes_agees_sedentaires)

tableau_hommes_ages_sedentaires = hommes_ages_sedentaires.tableau(dico_hommes_ages_sedentaires)

tableau_femmes_jeunes_sedentaires = femmes_jeunes_sedentaires.tableau(dico_femmes_jeunes_sedentaires)

tableau_hommes_jeunes_sedentaires = hommes_jeunes_sedentaires.tableau(dico_hommes_jeunes_sedentaires)

tableau_femmes_agees_sportives = femmes_agees_sportives.tableau(dico_femmes_agees_sportives)

tableau_hommes_ages_sportifs = hommes_ages_sportifs.tableau(dico_hommes_ages_sportifs)


#Création des instances:
#Creating instances

#Instances du niveau méthylation par âge et par le mode de vie (sédentaire ou sportif) en fonction du gène.

#Instances of the methylation level by age and lifestyle (sedentary or athletic) depending on the gene.

NPHP4 = Categorie_phenotypique(tableau_agees_sedentaires["NPHP4"],tableau_jeunes_sedentaires["NPHP4"],tableau_agees_sportives["NPHP4"])

MAEL = Categorie_phenotypique(tableau_agees_sedentaires["MAEL"],tableau_jeunes_sedentaires["MAEL"],tableau_agees_sportives["MAEL"])

cg00002837 = Categorie_phenotypique(tableau_agees_sedentaires["cg00002837"],tableau_jeunes_sedentaires["cg00002837"],tableau_agees_sportives["cg00002837"])

PINK1 = Categorie_phenotypique(tableau_agees_sedentaires["PINK1"],tableau_jeunes_sedentaires["PINK1"],tableau_agees_sportives["PINK1"])

#Instances du niveau méthylation par sexe, âge et par le mode de vie (sédentaire ou sportif) en fonction du gène.

#Instances of the methylation level by sex, age and lifestyle (sedentary or athletic) depending on the gene.

NPHP4s = Categorie_phenotypique2(tableau_femmes_agees_sedentaires ["NPHP4"],tableau_hommes_ages_sedentaires["NPHP4"],tableau_femmes_jeunes_sedentaires["NPHP4"], tableau_hommes_jeunes_sedentaires["NPHP4"],tableau_femmes_agees_sportives["NPHP4"],
tableau_hommes_ages_sportifs["NPHP4"])

MAELs = Categorie_phenotypique2(tableau_femmes_agees_sedentaires ["MAEL"],tableau_hommes_ages_sedentaires["MAEL"],tableau_femmes_jeunes_sedentaires["MAEL"], tableau_hommes_jeunes_sedentaires["MAEL"],tableau_femmes_agees_sportives["MAEL"],
tableau_hommes_ages_sportifs["MAEL"])

cg00002837s = Categorie_phenotypique2(tableau_femmes_agees_sedentaires ["cg00002837"],tableau_hommes_ages_sedentaires["cg00002837"],tableau_femmes_jeunes_sedentaires["cg00002837"], tableau_hommes_jeunes_sedentaires["cg00002837"],tableau_femmes_agees_sportives["cg00002837"],
tableau_hommes_ages_sportifs["cg00002837"])

PINK1s = Categorie_phenotypique2(tableau_femmes_agees_sedentaires ["PINK1"],tableau_hommes_ages_sedentaires["PINK1"],tableau_femmes_jeunes_sedentaires["PINK1"], tableau_hommes_jeunes_sedentaires["PINK1"],tableau_femmes_agees_sportives["PINK1"],
tableau_hommes_ages_sportifs["PINK1"])



#Application des méthodes:
#Application methods:

#Tableau du niveau méthylation par âge et par le mode de vie (sédentaire ou sportif) en fonction du gène.

#Table of the methylation level by age and lifestyle (sports or sports) depending on the gene.

tableau_NPHP4= NPHP4.table_concatener("âgées sédentaires","jeunes sédentaires","âgées sportives")

tableau_NPHP4 = tableau_NPHP4[0:12]

tableau_MAEL = MAEL.table_concatener("âgées sédentaires","jeunes sédentaires","âgées sportives")

tableau_MAEL=tableau_MAEL[0:52]

tableau_cg00002837=cg00002837.table_concatener("âgées sédentaires","jeunes sédentaires","âgées sportives")
tableau_cg00002837 =tableau_cg00002837[0:4]

tableau_PINK1= PINK1.table_concatener("âgées sédentaires","jeunes sédentaires","âgées sportives")

print(tableau_NPHP4)
print(tableau_MAEL)
print(tableau_cg00002837)
print(tableau_PINK1)

#Tableau du niveau méthylation par sexe, âge et par le mode de vie (sédentaire ou sportif) en fonction du gène.

#Table of the methylation level by sex, age and lifestyle (sedentary or athletic) depending on the gene.

tableau_NPHP4s= NPHP4s.table_concatener2("F âgées s","H âgés s","F jeunes s","H jeunes s"," F âgées sp", "H agés sp")


tableau_MAELs= MAELs.table_concatener2("F âgées s","H âgés s","F jeunes s","H jeunes s"," F âgées sp", "H agés sp")


tableau_cg00002837s= cg00002837s.table_concatener2("F âgées s","H âgés s","F jeunes s","H jeunes s"," F âgées sp", "H agés sp")


tableau_PINK1s= PINK1s.table_concatener2("F âgées s","H âgés s","F jeunes s","H jeunes s"," F âgées sp", "H agés sp")



print(tableau_NPHP4s)
print(tableau_MAELs)
print(tableau_cg00002837s)
print(tableau_PINK1s)

#Création des instances:
#Creating instances

#Instances Graphiques du niveau méthylation par âge et par le mode de vie (sédentaire ou sportif) en fonction du gène.

#Graphical instances of methylation level by age and lifestyle (sedentary or athletic) depending on the gene.

grapheNPHP4 = Graphique(tableau_NPHP4)
grapheMAEL= Graphique(tableau_MAEL)
graphecg00002837  = Graphique(tableau_cg00002837)
graphePINK1 = Graphique(tableau_PINK1)

#Instances Graphiques du niveau méthylation par sexe, âge et par le mode de vie (sédentaire ou sportif) en fonction du gène.

#Graphical instances of the methylation level by sex, age and lifestyle (sedentary or athletic) depending on the gene.

grapheNPHP4s = Graphique(tableau_NPHP4s[0:6])
grapheMAELs= Graphique(tableau_MAELs[0:26])
graphecg00002837s  = Graphique(tableau_cg00002837s[0:2])
graphePINK1s = Graphique(tableau_PINK1s)

#Application des méthodes:
#Application methods:

#Boxplot du niveau méthylation par âge et par le mode de vie (sédentaire ou sportif) en fonction du gène.

#Boxplot of methylation level by age and lifestyle (sedentary or sport) depending on the gene.

import matplotlib.pyplot as plt

plt.figure(1)

plt.subplot(2,2,1)

grapheNPHP4.boxplot("Niveau de méthylation de l'ADN sur gène NPHP4", "Niveau de méthylation de l'ADN")

plt.subplot(2,2,2)

grapheMAEL.boxplot("Niveau de  méthylation de l'ADN sur gène MAEL", "Niveau de méthylation de l'ADN")

plt.subplot(2,2,3)

graphecg00002837.boxplot("Niveau de méthylation de l'ADN sur la cg00002837", "Niveau de méthylation de l'ADN")

plt.subplot(2,2,4)

graphePINK1.boxplot("Niveau de méthylation de l'ADN sur gène PINK1", "Niveau de méthylation de l'ADN")

plt.gcf().subplots_adjust(left = 0.107, bottom = 0.2, right = 0.95, top = 0.9, wspace = 0.34, hspace = 0.35)

plt.savefig('graph1.png')

#Boxplot du niveau méthylation par sexe,  âge et par le mode de vie (sédentaire ou sportif) en fonction du gène.

#Boxplot of methylation level by sex, age and lifestyle (sedentary or athletic) depending on the gene.

import matplotlib.pyplot as plt

plt.figure(2)

plt.subplot(2,2,1)

grapheNPHP4s.boxplot2("Niveau de méthylation de l'ADN sur gène NPHP4", "Niveau de méthylation de l'ADN")

plt.subplot(2,2,2)

grapheMAELs.boxplot2("Niveau de  méthylation de l'ADN sur gène MAEL", "Niveau de méthylation de l'ADN")

plt.subplot(2,2,3)

graphecg00002837s.boxplot2("Niveau de méthylation de l'ADN sur la cg00002837", "Niveau de méthylation de l'ADN")

plt.text(1.7, 0.41, 'F: Femmes ; H: Hommes', style = 'italic',fontweight = 'bold', fontsize = 5.5, family = 'serif',color = "royalblue" )
plt.text(1, 0.40, 's:sédentaires ; sp: sportifs(ves)', style = 'italic',fontweight = 'bold', fontsize = 5.5, family = 'serif', color = "royalblue")

plt.subplot(2,2,4)

graphePINK1s.boxplot2("Niveau de méthylation de l'ADN sur gène PINK1", "Niveau de méthylation de l'ADN")

plt.gcf().subplots_adjust(left = 0.107, bottom = 0.2, right = 0.95, top = 0.9, wspace = 0.34, hspace = 0.35)


plt.savefig('graph2.png')




