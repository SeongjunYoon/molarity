import json


class ChemDict:
    def __init__(self, filename):
        self.filename = filename

    def read(self, reagent):
        try:
            with open(self.filename, 'r') as f:
                try:
                    # If there is a content in json file
                    chem_dict = json.load(f)
                except:
                    pass

                try:
                    return chem_dict[reagent]
                except:
                    print("'" + reagent + "'",
                          "does not exist in database.")
        except:
            print("No such filename.")

    def write(self, reagent_name, mol_weight):
        try:
            with open(self.filename, 'r') as f:
                try:
                    # If there is a content in json file
                    chem_dict = json.load(f)

                except:
                    # If json file is empty
                    chem_dict = {}

                finally:
                    if reagent_name in chem_dict:
                        print("'" + reagent_name + "'",
                              "Already exist in database.")
                    else:
                        chem_dict[reagent_name] = dict(Mw=mol_weight)

                    with open(self.filename, 'w', encoding='utf-8') as make_file:
                        json.dump(chem_dict, make_file, indent='\t')
        except:
            print("No such filename.")
