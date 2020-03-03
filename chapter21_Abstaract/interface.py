from abc import *
class DBInterface(ABC):
    @abstractmethod
    def connect(self):pass

    @abstractmethod
    def disconnect(self):pass

class Oracle(DBInterface):
    def connect(self):
        print('Connecting to Oracle Database...')
    def disconnect(self):
        print('Disconnecting to Oracle Database...')

class Sybase(DBInterface):
    def connect(self):
        print('Connecting to Sybase Database...')
    def disconnect(self):
        print('Disconnecting to Sybase Database...')

dbname=input("Enter Database Name:")
classname1=globals()[dbname] # The inbuilt function globals()[str] converts the string 'str' into a class name and returns the classname
obj=classname1()
obj.connect()
obj.disconnect()

