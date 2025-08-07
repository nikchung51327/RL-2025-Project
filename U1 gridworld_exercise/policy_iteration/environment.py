class Environment:

    def __init__(self):
        self.rT = self.create_rT()
    
    def create_rT(self):
        rT = {}
        for row in range(0,5):
            for col in range(0,5):
                key = (row, col)
                rT[key] = 0
        return rT
