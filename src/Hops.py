
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
        self.hop_list = []
        if hop_records:
            self.load_hops_from_records(hop_records)
        print(self.hop_list[0].__dict__)

    def add_hop(self, hop):
        self.hop_list.append(hop)

    def load_hops_from_records(self, hop_records):
        for record in hop_records:
            self.add_hop(Hop(record))

    def __repr__(self):
        return_str = 'Hops:\n'
        for hop in self.hop_list:
            return_str += f'  {hop}\n'
        return return_str
