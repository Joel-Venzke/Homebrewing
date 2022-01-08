
class Hop(object):
    """docstring for Hop."""

    def __init__(self,  record):
        super(Hop, self).__init__()
        self.name   = record['name']
        self.amount = record['amount']
        self.aau = record['aau']


    def __repr__(self):
        return f'{self.name} ({self.aau}): {self.amount}'

class Hops(object):
    """docstring for Hops."""

    def __init__(self, hop_records=None):
        super(Hops, self).__init__()
        self.hops = []
        if hop_records:
            self.load_hops_from_records(hop_records)

    def add_hop(self, hop):
        self.hops.append(hop)

    def load_hops_from_records(self, hop_records):
        for record in hop_records:
            self.add_hop(Hop(record))

    def __iter__(self):
        for key, value in self.__dict__.items():
            if key in ('hops'):
                records = []
                for val in value:
                    records.append(val.__dict__)
                yield (key, records)
            else:
                yield (key, records)

    def __repr__(self):
        return_str = 'Hops:\n'
        for hop in self.hops:
            return_str += f'  {hop}\n'
        return return_str
