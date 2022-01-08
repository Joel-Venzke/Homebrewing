from Recpies import Recpie


if __name__ == '__main__':
    grain_records = [
        {'name': '2-row Proximity', 'amount': 11},
        {'name': 'light DME', 'amount': 1},
        {'name': 'Flaked Rye Briess', 'amount': 1},
        {'name': 'Rice Hulls', 'amount': 0.4},
        {'name': 'Biscuit Proximity', 'amount': 0.275},
        {'name': 'Caramel Malet 6-row 60', 'amount':  0.275},
        {'name': 'Chocolate Bries', 'amount': 0.275},
        {'name': 'Roasted Barely Crips', 'amount': 0.275}
    ]
    fermentable_dict = {'grain': grain_records}

    hop_records = [{'name': 'citra', 'amount': 1.59, 'aau': 12.0}]

    recpie = Recpie('My beer', fermentable_dict, hop_records)
    print(recpie)
