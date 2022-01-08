class Grain(object):
    """docstring for Grain."""

    def __init__(self, record):
        super(Grain, self).__init__()
        self.name   = record['name']
        self.amount = record['amount']

    def __repr__(self):
        return f'{self.name}: {self.amount}'


class Fermentables(object):
    """docstring for Fermentables."""

    def __init__(self, fermentable_dict=None):
        super(Fermentables, self).__init__()
        self.grain = []
        if fermentable_dict:
            self.load_fermentables_from_dict(fermentable_dict)

    def add_grain(self, grain):
        self.grain.append(grain)

    def load_fermentables_from_dict(self, fermentable_dict):
        grain_records = fermentable_dict['grain']
        for record in grain_records:
            self.add_grain(Grain(record))

    def __iter__(self):
        for key, value in self.__dict__.items():
            if key in ('grain'):
                records = []
                for val in value:
                    records.append(val.__dict__)
                yield (key, records)
            else:
                yield (key, records)

    def __repr__(self):
        return_str = 'Grains:\n'
        for grain in self.grain:
            return_str += f'  {grain}\n'
        return return_str
