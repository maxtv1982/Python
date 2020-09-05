import unittest
from unittest.mock import patch
from Secretary import get_doc_owner_name, get_all_doc_owners_names, get_doc_shelf, delete_doc


class TestSomething(unittest.TestCase):

    def setUp(self):
        print("method setUp")

    def tearDown(self):
        print("method tearDown")

    def input(text):
        return input(text)

    @patch('Secretary.input', return_value='2207 876234')
    def test_get_doc_owner_name(self, input):
        self.assertEqual(get_doc_owner_name(), "Василий Гупкин")

    def test_get_all_doc_owners_names(self):
        self.assertEqual(get_all_doc_owners_names(), {'Аристарх Павлов', 'Василий Гупкин', 'Геннадий Покемонов'})

    @patch('Secretary.input', return_value="11-2")
    def test_get_doc_shelf(self, input):
        self.assertEqual(get_doc_shelf(), '1')

    # необходимо запускать отдельно
    # @patch('Secretary.input', return_value="11-2")
    # def test_delete_doc(self, input):
    #      self.assertEqual(delete_doc(), ('11-2', True))

if __name__ == '__main__':
    unittest.main()
