import helpers


class NearEarthObject:
    """This class represents a near earth object"""
    _fullname = None
    _designation = None
    _name = None
    _diameter = None
    _hazardous = None
    _approaches:list

    def __init__(self, designation, name, diameter, hazardous, approaches):
        self._designation = designation
        self._name = name
        self._diameter = diameter
        self._hazardous = hazardous
        self._approaches = approaches
        self._fullname = designation + "(" + name + ")"
        if len(name) == 0:
            self._fullname = designation

    @property
    def fullname(self):
        return self._fullname

    @fullname.setter
    def fullname(self,value):
        self._fullname = value

    @property
    def designation(self):
        return self._designation

    @designation.setter
    def designation(self, new_designation):
        self._designation = new_designation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,new_name):
        self._name = new_name

    @property
    def diameter(self):
        if(self._diameter != ''):
            return round(float(self._diameter),3)
        else:
            return "unknown"

    @diameter.setter
    def diameter(self,new_diameter):
        self._diameter = new_diameter

    @property
    def hazardous(self):
        return self._hazardous

    @hazardous.setter
    def hazardous(self, new_hazardous):
        self._hazardous = new_hazardous

    @property
    def approaches(self):
        return self._approaches

    @approaches.setter
    def approaches(self, new_approaches):
        self._approaches.append(new_approaches)

    def __str__(self):
        return ""+f'NEO {self._fullname} has a diameter of {self.diameter} km and {"is" if self.hazardous == True else "is not"} potentially hazardous'


class CloseApproach:
    """This class represents a close approach of a neo"""
    _time = None
    _distance = None
    _velocity = None
    _neo = None
    _designation = None
    _time_str = None
    temp_time = None

    def __init__(self, time, distance, velocity, neo, designation):
        self._time = time
        self.temp_time = time
        self._neo = neo
        self._distance = distance
        self._velocity = velocity
        self._designation = designation
        self._time_str = helpers.datetime_to_str(time)[1]


    @property
    def time(self):
        return self._time_str

    @time.setter
    def time(self, value):
        self._time = value

    @property
    def distance(self):
        if self._distance != '':
            return round(float(self._distance),3)
        else:
            return "unknown"

    @distance.setter
    def distance(self, value):
        self._distance = value

    @property
    def velocity(self):
        if self._velocity != '':
            return round(float(self._velocity),3)
        else:
            return "unknown"

    @velocity.setter
    def velocity(self, value):
        self._velocity = value

    @property
    def designation(self):
        return self._designation

    @designation.setter
    def designation(self, value):
        self._designation = value

    @property
    def neo(self):
        return self._neo

    @neo.setter
    def neo(self, value):
        self._neo = value

    @property
    def time_str(self):
        return helpers.datetime_to_str(self.temp_time)[0]

    def __str__(self):
        return f'On {self.time_str} ' \
               f' {self.designation} approaches Earth at a distance of {self.distance}' \
               f' au and a velocity of {self.velocity} km/s.'