from .db_base import SourceBase
from mysql import connector
from mysql.connector import errorcode

class SourceMysql(SourceBase):
    def __init__(self, **kwargs) -> None:
        super(SourceBase, self).__init__()

        self.client = self.connect_to_bd(**kwargs)
        

    def get_data(self, sql_query):
        """
        Fonction renvoyant les donnees sous la forme d'un dictionnaire
        {
            'nom_colonne': [valeur1, valeur2,]
        }
        """
        if self.client.is_closed:
            self.client.connect()

        cursor = self.client.connect()

        cursor.execute(sql_query)

        dict_to_return = self.convert_cursor_to_dict(cursor)

        cursor.close()
        self.client.close()

        return dict_to_return

    @staticmethod
    def convert_cursor_to_dict(cursor):
        """
        Fonction permettant de convertir le cursor en dictionnaire de la forme
        {
            'nom_colonne': [valeur1, valeur2,]
        }
        """
        dict_to_return = dict()

        for row in cursor:
            for key, values in row.items():
                dict_to_return[key] = dict_to_return.get(key, []) + [values,]

        return dict_to_return

    def connect_to_bd(self, **kwargs):
        connection = None
        try:
            connection = connector.connect(**kwargs)
        except connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        
        return connection