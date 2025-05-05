import datetime

class Bloque:
    def __init__(self , index , data , prevHash , difficulty = 4):
            self.index = index
            self.timestamp = datetime.time.strftime("%Y-%m-%d : %H-%M-%D")
            self.data = data
            self.prevHash = prevHash  
            self.nonce = 0 
            self.difficulty = difficulty
            self.hash = ...
            
    def calcularHash() : 
        ...
        
    def proofOfWork() : 
        ...
        