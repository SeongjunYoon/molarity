from chem_dict import ChemDict
import re


class Molarity:
    volume_dict = {
        'l': 1.0,
        'L': 1.0,
        'ml': 1e-3,
        'mL': 1e-3,
    }

    weight_dict = {
        'g': 1.0,
        'G': 1.0,
        'mg': 1e-3,
        'mG': 1e-3,
    }

    molarity_dict = {
        'M': 1.0,
        'mM': 1e-3,
    }

    def __init__(self, chem_dict):
        # Get chemical dictionary
        self.chem_dict = chem_dict

        # Select calculator
        calculator = input(
            "Select calculator (1. weight -> molarity / 2. molarity -> weight): ")

        if (calculator == "1"):
            self.weight2Molarity()

        elif (calculator == "2"):
            self.molarity2Weight()

        else:
            print("Enter 1 or 2 only!")

    def weight2Molarity(self):
        mol_weight = self.chemFinder()
        weight = self.valueFinder('weight')
        volume = self.valueFinder('volume')

        n = weight / mol_weight
        result = n / volume

        print("Samples' Mol concentration = {} M ({} mM)".format(
            f'{result:.4f}', f'{(result*1000):.4f}'))

    def molarity2Weight(self):
        mol_weight = self.chemFinder()
        molarity = self.valueFinder('molarity')
        volume = self.valueFinder('volume')

        n = molarity * volume
        result = n * mol_weight

        print("Samples' weight = {} g ({} mg)".format(
            f'{result:.4f}', f'{(result*1000):.4f}'))

    def valueFinder(self, phys):
        while True:
            if phys == 'volume':
                valueStr = input(
                    "Enter solvent volume (including unit: l / ml): ")
            elif phys == 'weight':
                valueStr = input(
                    "Enter sample weight (including unit: g / mg): ")
            elif phys == 'molarity':
                valueStr = input(
                    "Enter mol concentration (including unit: M / mM): ")
            else:
                pass

            l = re.findall(r"[-+]?\d*\.\d+|\d+", valueStr)

            for val in l:
                units = valueStr.replace(val, '')

            units = units.split()

            try:
                # Take only the first input value
                value = float(l[0])
                unit = str(units[0])

                try:
                    if phys == 'volume':
                        const = self.volume_dict[unit]
                    elif phys == 'weight':
                        const = self.weight_dict[unit]
                    elif phys == 'molarity':
                        const = self.molarity_dict[unit]
                    else:
                        pass
                except:
                    if phys == 'volume':
                        print("Wrong unit (enter only 'l', 'L', 'ml', 'mL')")
                    elif phys == 'weight':
                        print("Wrong unit (enter only 'g', 'G', 'mg', 'mG')")
                    elif phys == 'molarity':
                        print("Wrong unit (enter only 'M', 'mM')")
                    else:
                        pass

                return (value * const)

            except:
                print("Conversion error! Try again")

    def chemFinder(self):
        reagent = input("Enter molecule : ")
        mol_weight = self.chem_dict.read(reagent)['Mw']
        print("Molecular weight =", mol_weight)
        return mol_weight


if __name__ == "__main__":
    chem_dict = ChemDict('chem_dict.json')
    mol_cal = Molarity(chem_dict)
