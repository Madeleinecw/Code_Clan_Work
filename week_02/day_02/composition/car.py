
class Car:

    def __init__(self, make, model, engine, gearbox):
        self.make = make
        self.model = model
        self.engine = engine
        self.gearbox = gearbox

    def start(self):
        return self.engine.start() 
    
    def change_gear(self):
        return self.gearbox.change_gear(gear)un