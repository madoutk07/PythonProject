from unittest import TestCase
from Model.Patterns import FactoryPattern
class TestFactoryPattern(TestCase):
    def test_create_product(self):
        # Créer une instance de FactoryPattern
        factory = FactoryPattern()

        # Appeler la méthode create_product() et vérifier le résultat
        product = factory.create_product()
        self.assertIsNotNone(product)
        self.assertIsInstance(product, str)

