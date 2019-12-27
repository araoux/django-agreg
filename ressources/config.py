

def renommage(instance, nom_fichier):
    return "ressources/{}s/{}-{}".format(instance.__class__.__name__,instance.id, nom_fichier)
