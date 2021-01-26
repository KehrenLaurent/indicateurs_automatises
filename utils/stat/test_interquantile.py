"""
Test en fonction de l'exemple de ce site :
https://fr.khanacademy.org/math/be-4eme-secondaire2/x213a6fc6f6c9e122:statistiques-1/x213a6fc6f6c9e122:diagramme-en-boite-et-ecart-interquartil/a/identifying-outliers-iqr-rule

"""

from unittest import TestCase
from .interquantile import Interquantile
import numpy as np

class InterquantileTestCase(TestCase):
    
    def setUp(self):
        self.values = [5, 7, 10, 15, 19, 21, 21, 22, 22, 23, 23, 23, 23, 23, 24, 24, 24, 24, 25]
        self.interquantile = Interquantile(self.values)

    def test_init(self):
        self.values.sort()
        self.assertListEqual(
            self.values,
            self.interquantile.data.tolist()
        )

    def test_get_mediane(self):
        self.assertEqual(23, self.interquantile.get_mediane())

    def test_get_premier_quantile(self):
        self.assertEqual(19, self.interquantile.get_premier_quantile())

    def test_get_troisieme_quantile(self):
        self.assertEqual(24, self.interquantile.get_troisieme_quantile())

    def test_get_ecart_interquantile(self):
        self.assertEqual(5, self.interquantile.get_ecart_interquantile())

    def test_get_borne_inferieure(self):
        ecart_interquantile = self.interquantile.get_ecart_interquantile()
        self.assertEqual(11.5, self.interquantile.get_borne_inferieure(ecart_interquantile))

    def test_get_borne_superieure(self):
        ecart_interquantile = self.interquantile.get_ecart_interquantile()
        self.assertEqual(31.5, self.interquantile.get_borne_superieure(ecart_interquantile))

    def test_get_data_sans_valeurs_abherrantes(self):
        li = 11.5
        ls = 31.5
        sansAbhe = [v for v in filter(lambda x: x>= li and x<= ls, self.values)]

        ecart_interquantile = self.interquantile.get_ecart_interquantile()
        borne_inferieure = self.interquantile.get_borne_inferieure(ecart_interquantile)
        borne_superieure = self.interquantile.get_borne_superieure(ecart_interquantile)

        self.assertListEqual(
            sansAbhe, 
            self.interquantile.get_data_sans_valeurs_abherrantes(borne_inferieure, borne_superieure).tolist()
        )
        
