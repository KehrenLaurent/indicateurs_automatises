from abc import abstractmethod, ABCMeta

class SourceBase(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_data():
        """
        Fonction a implementer qui renvoi les donnees de la base de donnees
        """
        pass

class DestionnationBase(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def insert_values():
        """ 
        Method a implementer permettant d'ajouter les valeurs dans la base de donnees
        """
        pass

class IndicateurBase(object):
    def __init__(self, source: SourceBase, destionnation: DestionnationBase):
        super(IndicateurBase, self).__init__()

        self.source = source
        self.destionnation = destionnation

    @abstractmethod
    def preparer_data_pour_destionnataire(data_source):
        """
        Fonction qui preparer les donnees à envoyer au destinnaire
        """
        pass

    def calculer_indicateur(self):
        """
        method qui fait les operations suivantes
            -> recuperer les donnes de la source
            -> met en forme les donnees
            -> envoi les donnees a la source destinataire
        """
        source_data = self.source.get_values()
        destionnation_data = self.preparer_data_pour_destionnataire(source_data)
        self.destionnation.insert_values(destionnation_data)

    

    