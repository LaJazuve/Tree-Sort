#####clean Code Tree

import os, os.path,shutil
import glob
import tkinter as tk
from tkinter.filedialog import askdirectory as ask
import pickle

##dans l'ordre :

####1/ Root_demande de repertoire (entrant et sortant)
####2/ Trunk_outil scan et listing
#####3/ Sap_confirmation et supervision fichier
#####4/ Branch_confirmation scan sous dossier
######5/ Leaf_déplacement et copie

#retour menue

class Tree:

    def __init__(self,Root,Sky,Bark,delR):

        self.Root=''
        self.Sky=''
        self.Bark={}
        self.delR=''




    def Rootrp(self):
        
        videur=False
        while videur is False:
            
            rp=input("Ecrire chemin du répertoir source.")

            bol=os.path.exists(rp)

            if bol is True:
                self.delR=rp
                rp+=("\*")
                self.Root=rp
                self.delR=rp
                print (self.Root)
                videur = True
            
            elif bol is False:
                print("Ce répertoire n'existe pas, recommencer")
            


         
    def Skyrp (self):
        
        videur = False
        while  videur is False:
            
            rp=input("Ecrire chemin du répertoir de sorti.")
            
            if os.path.exists(rp) == False:
                print ("ce repertoire n'existe pas, recommencer.")

            else:
                videur = True
            
        rpp=(rp+"\Tree")
        if os.path.split(rp[1]) == ("Tree"):
            print ("le répertoire ",rp," existe déjà, les nouveaux fichier y seront ajouter")
            self.Sky=rpp

        elif os.path.exists(rpp) is True :
            self.Sky=rpp
            print ("le répertoire ",rpp," existe déjà, les nouveaux fichier y seront ajouter")
                
        else:

            rp+=("\Tree")
            os.makedirs(rp)
            print ("Le Repertoire ",rp," a été crée\n")
            self.Sky=rp


    
        
    def Trunk (self):

        liste=glob.glob(self.Root)
    
        for file in liste:
            
            if os.path.isfile(file) is True:
                
                ex=os.path.splitext(file)
                print(ex)
                
                ext=ex[1]
                ext=ext.replace(".","")
                if ext==(''):
                    ext="inconnu"
                
                
                if self.Bark.__contains__(ext)is False:
                    self.Bark[ext]=[file]
                    
                elif self.Bark.__contains__(ext) is True:
                    self.Bark[ext].append(file)
                
            elif os.path.isdir(file) is True:
               
                if self.Bark.__contains__("folder") is False:
                    self.Bark["folder"]=[file]

                elif self.Bark.__contains__("folder") is True:
                    self.Bark["folder"].append(file)



    def Branch(self):

        for key in self.Bark:

            if key !=("folder"):
                
                print (key,"\n\n")
                i=1
                
                for file in self.Bark[key]:
                    print (i," - ",file,"\n")
                    i+=1

    def Sap (self):

        videur=False
        while videur is False:

            print("Voici la liste des fichier trouver.\nsi vous voulez que certain fichier ne soit pas déplacer écrivez l'extension puis sont numéro de liste séparer d'un point \n ex : jpg.3,\n ou si vous avez fini ecrire 'fin'.")
            print ("\n'all.ext*' pour retirer tout les elements d'une extension\n")
            choose=input()

            if choose == "fin":
                videur = True

            elif choose =="quitter":
                quit()

            else:
                choose=choose.split(".")

                if choose[0]=="all":
                    del self.Bark[choose[1]]
                    print ("Aucun ",choose[1]," ne sera déplacé.")
                else:
                    
                    choose[1]=int(choose[1])
                    choose[1]= choose[1]-1
                    print (self.Bark[choose[0]][choose[1]]," ne sera pas déplacer")
                    del self.Bark[choose[0]][choose[1]]

  



    
    def Leaf (self):

        FolderTree=self.Sky
            
        for key in self.Bark:
            
            if key !=("folder"):
                print (key)
                slash="\ "
                slash.replace(" ","")
                
                direct=(FolderTree+slash+key)
            
                if os.path.exists(direct) is False:
                    os.makedirs(direct)
                    print ("Le répertoire ",direct," a été crée\n")
                for F in self.Bark[key]:
                    
                    Fdirect=(direct+slash+os.path.basename(F))
                    Fdirect.split("\\")
                    Fdirect.join(slash)
                    try:
                        shutil.move(F,Fdirect)
                    except PermissionError or FileExistsError:
                        
                        if os.path.exists(FolderTree+slash+"Errors") is False:
                            os.makedirs(FolderTree+slash+"Errors")
                        
                        with open((FolderTree+slash+"Errors"+"/errors.txt"),'wb')as fichier:
                            pick=pickle.Pickler(fichier)
                            pick.dump(F)
                        
                        print ("\n Error!!!!!!!!!!!!!!")
                    print("Le fichier ",os.path.basename(Fdirect)," à été traiter avec succés!\n")


    def Spirit(self,bol):

        if bol is True:
            print(self.Bark)
            self.Leaf()
            

        elif bol is False:

            
            self.Bark["folder"][0]+=("\*")
            self.Root=self.Bark["folder"][0]
            print (self.Bark["folder"][0], " va être scanner.")
            del self.Bark["folder"][0]
            return False


    def Allyess(self):
        bol=False
        self.Spirit(bol)
        while bol is False:
            
            self.Trunk()
            if self.Bark.__contains__("folder") is False or len(self.Bark["folder"])==0:
                bol=True
            self.Spirit(bol)
        
    def Twig (self):

        videur = False
        while videur is False:

            if self.Bark.__contains__("folder") is False or len(self.Bark["folder"])==0:

                print ("aucun sous dossier détecter, le programme va démarrer")
                videur =True
                return True #lance le deplacement
            
            else:
                i=1
                for file in self.Bark["folder"]:
                    print (i,file)
                    i+=1
                    
                if self.Bark.__contains__("Dir") is True:
                    i=1
                    print("\n\n Fichier a Deplacer\n")
                    for file in self.Bark["Dir"]:
                        print (i,file)
                        i+=1
                        
                choose=input("Voici la liste des sous dossier présent, lequel voulez vous traiter ? \n mettre les numeros des dossier a NE PAS traiter, UN PAR UN.\n c-n° pour deplacer le dossier\nsi aucun taper 'rien' une fois fini taper 'fin' le programme de trie démarrera.")

                if choose == "fin":
                        videur = True
                        return False #retourne au scan et ajoute les nouveau fichier

                elif choose=="rien":
                    del self.Bark["folder"]
                          
                elif choose=="allyes":
                    self.Allyess()
                    videur =True
                    

                elif choose =="quitter":
                    quit()
#rajout
                elif choose.split("-")[0]=="c":
                    choose=choose.split("-")[1]
                    choose=int(choose)
                    choose=choose-1
                    print(self.Bark["folder"][choose], " sera copié sans etre trié")
                    
                    if self.Bark.__contains__("Dir") is False:
                        self.Bark["Dir"]=[self.Bark["folder"][choose]]
                        del self.Bark["folder"][choose]

                    elif self.Bark.__contains__("Dir") is True:
                        self.Bark["Dir"].append(self.Bark["folder"][choose])
                        del self.Bark["folder"][choose]
#
                else:
                    choose=int(choose)
                    choose=choose-1
                    print (self.Bark["folder"][choose]," ne sera pas trié")
                    del self.Bark["folder"][choose]

