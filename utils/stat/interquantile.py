"""
Module permettant d'eliminer les valeurs abherantes d'une serie np a l'aide du test interquantile
Le test est presente sur le site :
https://fr.khanacademy.org/math/be-4eme-secondaire2/x213a6fc6f6c9e122:statistiques-1/x213a6fc6f6c9e122:diagramme-en-boite-et-ecart-interquartil/a/identifying-outliers-iqr-rule

"""
from pdb import post_mortem
import numpy as np

class Interquantile(object):

    def __init__(self, list_data):
        """
        list_data : list contenant les valeurs
        """
        if not isinstance(list_data, list):
            raise ValueError("Vous devez donner une liste")

        # donnees en np.array, puis trie des valeurs
        self.data = np.array(list_data)
        self.data.sort()

    def get_mediane(self):
        """
        Donne la valeur de la mediane
        """
        position = int(self.data.size/2)
        return self.data[position]

    def get_premier_quantile(self):
        """
        Donne la valeur du premier quantile
        """
        position = int(self.data.size/4)
        return self.data[position]

    def get_troisieme_quantile(self):
        """
        Donne la valeur du troiseme quantile
        """
        position = int(self.data.size/4) + 1
        return self.data[-position]

    def get_ecart_interquantile(self):
        """
        Donne la valeur de l'ecart interquantile
        """
        return self.get_troisieme_quantile() - self.get_premier_quantile()

    def get_borne_inferieure(self, ecart_interquantile):
        """
        Donne la limite inferieure
        """
        return self.get_premier_quantile() - 1.5 * ecart_interquantile

    def get_borne_superieure(self, ecart_interquantile):
        """
        Donne la limite superieure
        """
        return self.get_troisieme_quantile() + 1.5 * ecart_interquantile

    def get_data_sans_valeurs_abherrantes(self, borne_inferieure, borne_superieure):
        """
        Return un np_array sans les valeurs abherrantes
        """
        dataSansAbhe = self.data[self.data<=borne_superieure]
        dataSansAbhe = dataSansAbhe[dataSansAbhe>=borne_inferieure]
        return dataSansAbhe