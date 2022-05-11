

class NEODatabase:
    _neos = None
    _approaches = None
    _neo_and_designation_dictionary = None
    _neo_and_name_dictionary = None
    _approach_and_designation_dictionary = None

    def __init__(self, neos, approaches):
        self._neos = neos
        self._approaches = approaches


        """Fetching approaches with designations in a dictionary"""
        self._approach_and_designation_dictionary = \
            {approach.designation: approach for approach in self._approaches}
        """Fetching neo objects in a dictionary according to designation"""
        self._neo_and_designation_dictionary = \
            {neo.designation: neo for neo in self._neos}
        """Fetching neo objects according to names in a dictionary"""
        self._neo_and_name_dictionary = \
            {neo.name: neo for neo in self._neos}
        """Traversing through neo and approaches objects to set 
        corresponding values of neo objects and 
        approaches objects"""
        keys_of_approach_and_designation_dictionary = \
            self._approach_and_designation_dictionary.keys()
        keys_of_neo_and_designation_dictionary = \
            self._neo_and_designation_dictionary.keys()
        for approach_key in keys_of_approach_and_designation_dictionary:
            for neo_key in keys_of_neo_and_designation_dictionary:
                if approach_key == neo_key:
                    self._approach_and_designation_dictionary[approach_key].neo = \
                        self._neo_and_designation_dictionary[neo_key]
                    self._neo_and_designation_dictionary[neo_key].approaches = \
                        self._approach_and_designation_dictionary[approach_key]

    def get_neo_by_designation(self, designation):
        neo_with_designation = {neo_des: neo_obj for (neo_des, neo_obj)
                                in self._neo_and_designation_dictionary.items()
                                if neo_des == designation}
        return neo_with_designation[designation]

    def get_neo_by_name(self, name):
        neo_by_name = {neo_name: neo_obj for (neo_name, neo_obj)
                       in self._neo_and_name_dictionary.items()
                       if neo_name == name}
        return neo_by_name[name]

