#Practice final2

class Frequent_Flyer:
    
    def __init__ (self, name):
        self.name = name
        self.flights = []
        self.miles = 0
    def flight(self,origin,destination,miles):
        self.flights.append((origin,destination,miles))
        self.miles += miles
        
    def __str__(self):
        return "%s has %d miles on flights: %s" %(self.name,self.miles,str(self.flights))

        