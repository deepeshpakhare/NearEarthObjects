import database
import helpers
from models import NearEarthObject
import extract
import argparse


if __name__ == '__main__':
    neos = extract.load_neos(r"data/neos.csv")
    approaches = extract.load_approaches(r"data/cad.json")
    database_object = database.NEODatabase(neos, approaches)

    parser = argparse.ArgumentParser()
    parser.add_argument("inspect", nargs='?',
                        help="Inspect an NEO by primary designation or by name")
    parser.add_argument("--pdes", nargs=1,
                        help="The primary designation of the NEO to inspect")
    parser.add_argument("--name", nargs=1,
                        help="The name of the NEO to inspect")
    parser.add_argument("--verbose", nargs='?',
                        help="To know the info about neo and its approaches")
    args = parser.parse_args()
    neo_by_name = ""
    if args.pdes is not None:
        neo_by_designation = database_object.get_neo_by_designation(args.pdes[0])
        print(neo_by_designation)
    if args.name is not None:
        neo_by_name = database_object.get_neo_by_name(args.name[0])
        print(neo_by_name)
    if args.verbose is None:
        print(len(neo_by_name.approaches))
