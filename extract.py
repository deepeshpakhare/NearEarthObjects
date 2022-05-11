import csv
import json

import models
from models import NearEarthObject


def load_neos(neo_csv_path):
    neo_objects = []
    column_name_to_number_dictionary = {"designation": None, "name": None, "diameter": None, "hazardous": None}
    column_number_counter = -1
    with open(neo_csv_path, "r") as infile:
        data = csv.reader(infile)
        all_columns = [columns for columns in next(data)]
        for column in all_columns:
            column_number_counter += 1
            if column == "pdes":
                column_name_to_number_dictionary["designation"] = column_number_counter
            if column == "name":
                column_name_to_number_dictionary["name"] = column_number_counter
            if column == "diameter":
                column_name_to_number_dictionary["diameter"] = column_number_counter
            if column == "pha":
                column_name_to_number_dictionary["hazardous"] = column_number_counter

        for row in data:
            designation_of_object = row[column_name_to_number_dictionary["designation"]]
            name_of_object = row[column_name_to_number_dictionary["name"]]
            diameter_of_object = row[column_name_to_number_dictionary["diameter"]]
            hazardous_or_not = row[column_name_to_number_dictionary["hazardous"]]
            if hazardous_or_not == "Y":
                boolean_hazardous = True
            else:
                boolean_hazardous = False
                empty_list = list()
            neo_objects.append(NearEarthObject(designation_of_object, name_of_object,
                                               diameter_of_object, boolean_hazardous,empty_list))

    return neo_objects


def load_approaches(cad_jason_path):
    close_approaches = []
    fields_to_indexes_of_fields_dictionary = {"time": None, "distance": None, "velocity": None, "designation": None}
    index_counter = -1
    with open(cad_jason_path, "r") as infile:
        data = json.load(infile)
        fields = data["fields"]
        for field in fields:
            index_counter += 1
            if field == "des":
                fields_to_indexes_of_fields_dictionary["designation"] = index_counter
            if field == "cd":
                fields_to_indexes_of_fields_dictionary["time"] = index_counter
            if field == "dist":
                fields_to_indexes_of_fields_dictionary["distance"] = index_counter
            if field == "v_rel":
                fields_to_indexes_of_fields_dictionary["velocity"] = index_counter

        for list_element in data["data"]:
            destination_of_close_approach = list_element[fields_to_indexes_of_fields_dictionary["designation"]]
            time_of_close_approach = list_element[fields_to_indexes_of_fields_dictionary["time"]]
            distance_of_close_approach = list_element[fields_to_indexes_of_fields_dictionary["distance"]]
            velocity_of_close_approach = list_element[fields_to_indexes_of_fields_dictionary["velocity"]]
            close_approaches.append(models.CloseApproach(time_of_close_approach, distance_of_close_approach,
                                                         velocity_of_close_approach,
                                                         None,
                                                         destination_of_close_approach))

    return close_approaches

