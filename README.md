# data-analysis-on-Methylation450K-BeadChip-Illumina-pandas-matplotlib-
Graphic representation : Boxplot

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
