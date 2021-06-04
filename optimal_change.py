import math
def optimal_change(item_cost, amount_paid):

  currency = [100,50,20,10,5,1,.25,.10,.05,.01]

  amount_due = float(amount_paid - item_cost)
  holding_ground = f'The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is '

  if amount_due > 0:
    for i in range(len(currency)):
      times_how_many = math.floor(amount_due // currency[i])
      #where you account for single/plural
      if i >= 6 and times_how_many > 0:
        holding_ground += f'{times_how_many} ${currency[i]} cent '
        amount_due -= (times_how_many * currency[i])
        break
      if times_how_many > 0:
        holding_ground += f'{times_how_many} ${currency[i]} bill '
        amount_due -= (times_how_many * currency[i])
       
  return holding_ground
print(optimal_change(1, 7.85))