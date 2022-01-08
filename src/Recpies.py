from Fermentables import Fermentables, Grain
from Hops import Hops, Hop
import json

class Recpie(object):
    """docstring for Recpie."""

    def __init__(self, name=None, fermentable_dict={}, hop_records={}, yeast_records={}, mash_profile_records={}):
        super(Recpie, self).__init__()
        self.name = name
        self.load_fermentables_from_dict(fermentable_dict)
        self.load_hops_from_records(hop_records)
        # self.yeast = yeast_records
        # self.mash_profile = mash_profile_records

    def load_fermentables_from_dict(self, fermentable_dict):
        self.fermentables = Fermentables(fermentable_dict)

    def load_hops_from_records(self, hop_records):
        self.hops = Hops(hop_records)

    def save_json(self, file_name):
        recpie_dict = dict(self)
        with open(file_name, "w") as outfile:
            json.dump(recpie_dict, outfile)

    def load_from_dict(self, recpie_dict):
        for key, value in recpie_dict.items():
            if key == 'fermentables':
                self.load_fermentables_from_dict(value)
            elif key == 'hops':
                self.load_hops_from_records(value['hops'])
            else:
                self.__dict__[key] = value

    def load_json(self, file_name):
        with open(file_name, "r") as outfile:
            recpie_dict = json.load(outfile)
            self.load_from_dict(recpie_dict)

    def __iter__(self):
        for key, value in self.__dict__.items():
            if key in ('fermentables', 'hops'):
                yield (key, dict(value))
            else:
                yield (key, value)

    def __repr__(self):
        return_str = f'Recpie: "{self.name}"\n'
        return_str += '-'*(len(return_str)-1)+'\n'
        return_str += str(self.fermentables)
        return_str += str(self.hops)
        return return_str
