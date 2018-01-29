class Settings:
    #Constructor
    def __init__(self, file_name):
        #Imports
        import pickle
        import zlib
        import os

        self.__FileName = file_name

        if os.path.isfile(file_name):
            f = open(self.__FileName, "rb")
            compressed_data = f.read()
            f.close()
            pickled_data = zlib.decompress(compressed_data)
            self.__Data = pickle.loads(pickled_data)
        elif not os.path.isfile(file_name):
            self.__Data = {}

            
    #Destructor  
    def __del__(self):
        self.SaveChanges()

    def Close(self):
        self.SaveChanges()

    #If a variable doesn't exist, it is created.
    def SetVariable(self, variable_name, variable_value):
        self.__Data[variable_name] = variable_value

    def GetVariable(self, variable_name):
        try:
            return self.__Data[variable_name]
        except:
            return None

    def SaveChanges(self):
        import pickle
        import zlib
        #Puts it into a binary format of the object (dictionary)
        #Highest Protocol is the most efficient
        pickled_data = pickle.dumps(self.__Data, pickle.HIGHEST_PROTOCOL)
        #9 is the most efficient, but slightly slower
        compressed_data = zlib.compress(pickled_data, 9)
        f = open(self.__FileName, "wb")
        f.write(compressed_data)
        f.close()
