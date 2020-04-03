import mysql.connector
from helpers.test_logger import TestLogger
from mysql.connector import Error, MySQLConnection


class DbConnection(MySQLConnection):
    #connection = None
    #HOST = '127.0.0.1'
    #USER_NAME = 'root'
    #PASSWORD = 'Qwerty123'

    def __init__(self, host_name, user_name, user_password, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host_name,
                user=self.user_name,
                password=self.user_password
            )
            TestLogger.get_logger().info('Connection to MySQL DB successful')
        except Error as e:
            TestLogger.get_logger().error(f'The error {e} occurred')

        return self.connection

    def close_connection(self):
        try:
            if self.connection.is_connected():
                self.connection.close()
                info = ''.join(self.connection.server_host)
                TestLogger.get_logger().info(f'Connection {info} was closed')
                print(type(self.connection))
        except Error as e:
            TestLogger.get_logger().error(f'The error {e} occurred, connection was not closed')



conn = DbConnection()










