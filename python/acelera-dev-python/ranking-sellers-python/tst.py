# tst.py
from operator import itemgetter
from main import SellersRancking
sellers = [
    {"name": "Joaquina", "store": 2, "value": 1200.00},
            {"name": "Pedro", "store": 2, "value": 120.00},
            {"name": "Maria", "store": 1, "value": 450.00},
            {"name": "Fernanda", "store": 1, "value": 4000.00},
            {"name": "Patricia", "store": 1, "value": 100.00},
]

sr = SellersRancking()

# print(sr.rancking_list(sellers))
# sorted_list = sorted(sellers, key=itemgetter('value'), reverse=True)
# print([seller['name'] for seller in sorted_list])
# print(sr.sales_goals(sellers))

# sorted_sellers = filter(lambda seller: seller['value'] < 500, sorted(
#     sellers, key=itemgetter('value')))
# print([seller['name'] for seller in sorted_sellers])

# sorted_list = sorted(
#     list(filter(lambda x: x['value'] < 500, sellers)), key=itemgetter('value'))
# print([dicts['name'] for dicts in sorted_list])

store = 2
print(list(filter(lambda x: x['store'] == store,sorted(sellers,key=itemgetter('value'),reverse=True))))