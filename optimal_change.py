import math
def optimal_change(item_cost, amount_paid):

  currency = [100,50,20,10,5,1]
  denomination = ['Hundred', 'Fifty', 'Twenty', 'Ten', 'Five,', 'One']

  amount_due = amount_paid - item_cost
  holding_ground = []

  if amount_due > 0:
    for i in range(len(currency)):
      times_how_many = math.floor(amount_due // currency[i])
      if times_how_many > 0:
        print(times_how_many)
        amount_due -= times_how_many * currency[i]

print(optimal_change(10, 20))