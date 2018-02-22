import sys
import glob
import json
import jsonschema

class Validator:
    def __init__(self, schema):
        with open(schema, 'r') as fd:
            self.schema = json.load(fd)

    def check(self, data):
        with open(data, 'r') as fd:
            data = json.load(fd)
            jsonschema.validate(data, self.schema)

def validate_all_json(dir, schema, debug=False):
    validator = Validator(schema)
    for jsonfile in glob.glob(dir):
        if debug:
            out = 'validating: {}\n'.format(jsonfile)
            sys.stdout.write(out)
        validator.check(jsonfile)

degree = lambda debug: validate_all_json('../degree/*', './degree.schema.json', debug=debug)
domestic = lambda debug: validate_all_json('../domestic/*', './domestic.schema.json', debug=debug)
international = lambda debug: validate_all_json('../international/*', './international.schema.json', debug=debug)
journal = lambda debug: validate_all_json('../journal/*', './journal.schema.json', debug=debug)

if __name__ == '__main__':
    debug = True
    degree(debug)
    domestic(debug)
    international(debug)
    journal(debug)
