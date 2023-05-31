class NationalPark:


    def __init__(self, name):
        self.name = name
        self._trips = []
        self._visitors = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        # test messes this up and both of them require this conditional
        if not hasattr(self, 'name') and isinstance(name, str) and 1<= len(name) <= 15:
            self._name = name
        else:
            raise Exception 
    
        
    def trips(self, new_trip=None):
        from classes.trip import Trip
        # also forgot to add new_trip to check it wasincluded beofre i add to list 
        if new_trip and isinstance(new_trip, Trip):
            self._trips.append(new_trip)
        return self._trips
        pass
    
    def visitors(self, new_visitor=None):
        from classes.visitor import Visitor
        if isinstance(new_visitor, Visitor):
            # new_visitor not in self._visitors and takend out 
            self._visitors.append(new_visitor)
        return set(self._visitors)
        pass
    
    def total_visits(self):
        return len(self._trips)
        pass
    
    def best_visitor(self):
        return max(set(self._visitors), key=self._visitors.count)
        # visitor = None
        # visitamnt = 0 
        # for v in self._visitors:
        #     visits = self._visitors.count(v)
        #     if visits > visitamnt:
        #         visitor = v
        #         visitamnt = visits
        # return visitor
    # rabs main from the 
        pass

dandelion = NationalPark("becca")
