class Visitor:

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._parkList = []
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        # test messes this up and both of them require this conditional
        if isinstance(name, str) and not hasattr(self, 'name')  and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception('Wtf dawg')
    
    
    def trips(self, new_trip=None):
        from classes.trip import Trip
        if new_trip and isinstance(new_trip, Trip):
            self._trips.append(new_trip)
        return self._trips
        pass
    
    def national_parks(self, new_national_park=None):
        from classes.national_park import NationalPark
        if new_national_park not in self._parkList and isinstance(new_national_park, NationalPark):
            self._parkList.append(new_national_park)
        return self._parkList
        pass

