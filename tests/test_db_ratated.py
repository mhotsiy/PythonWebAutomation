from helpers.db_connector import ConnectDb


class TestDBRelated:

    def test_connection_to_db_is_successfull:
        connection = ConnectDb.create_connection()
