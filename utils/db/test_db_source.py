from unittest import TestCase
from .db_source import SourceMysql

class SourceMysqlTestCase(TestCase):
    def test_convert_cursor_to_dict(self):
        "Test que la mise en forme des donnees est respecte"
        cursor = [
            {'key1': 'values 1', 'key2': 'values 2'},
            {'key1': 'values 1', 'key2': 'values 2'},
        ]

        convert_data = SourceMysql.convert_cursor_to_dict(cursor)

        self.assertTrue(type(convert_data) is dict)
        self.assertTrue(type(convert_data['key1']) is list)
        self.assertListEqual(
            [key for key in convert_data.keys()],
            ['key1', 'key2']
        )
        self.assertListEqual(
            convert_data['key1'],
            ['values 1', 'values 1']
        )
        self.assertListEqual(
            convert_data['key2'],
            ['values 2', 'values 2']
        )