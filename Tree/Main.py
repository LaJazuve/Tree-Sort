import Tree
import os



prog=Tree.Tree('','',{},0)

prog.Rootrp()
prog.Skyrp()
bol=False

while bol is False:
    prog.Trunk()
    prog.Branch()
    prog.Sap()
    bol=prog.Twig()
    bol=prog.Spirit(bol)

os.system("pause")
###accepter tout les sous dossier déjà présenter et
###ne juste montrer que les nouveaux fichier du repertoire traiter
###les nouveaux sous dossier seront traiter à la fin 
