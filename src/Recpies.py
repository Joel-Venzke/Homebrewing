from Fermentables import Fermentables, Grain
from Hops import Hops, Hop

class Recpie(object):
    """docstring for Recpie."""

    def __init__(self, name, fermentable_dict={}, hop_records={}, yeast_records={}, mash_profile_records={}):
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

    def __repr__(self):
        return_str = f'Recpie: "{self.name}"\n'
        return_str += '-'*(len(return_str)-1)+'\n'
        return_str += str(self.fermentables)
        return_str += str(self.hops)
        return return_str
