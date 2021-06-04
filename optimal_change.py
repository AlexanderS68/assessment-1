import math

def optimal_change(item_cost, amount_paid):
  #List of currencies
  currency = [100,50,20,10,5,1,.25,.10,.05,.01]

  #Variable to hold the difference between amount owed and amount paid to
  amount_due = float(amount_paid - item_cost)

  #Variable holding opening statement and to append currency amount and type
  holding_ground = f'The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is'

  #Check that both inputs are an integer or float
  if item_cost == int or amount_paid == int:
    return('Input a valid integer or float')
  
  #Check that paid amount is enough
  if amount_paid < item_cost:
    return('Insufficent funds')

  #A check if any amount needs to be taken away from
  if amount_due > 0:
    for i in range(len(currency)):
      times_how_many = math.floor(amount_due // currency[i])
      #If statement to check if remainder is higher than one to account for singular or plural
      if times_how_many > 1:
        if i >= 6 and times_how_many > 0:
          holding_ground += f', {times_how_many} ${currency[i]} cents'
          amount_due -= (times_how_many * currency[i])
          continue
        elif times_how_many > 0:
          holding_ground += f', {times_how_many} ${currency[i]} bills'
          amount_due -= (times_how_many * currency[i])
      #Same check for remainder/ singular,plural
      elif times_how_many > 0:
        if i >= 6 and times_how_many > 0:
          holding_ground += f', {times_how_many} ${currency[i]} cent'
          amount_due -= (times_how_many * currency[i])
          continue
        elif times_how_many > 0:
          holding_ground += f', {times_how_many} ${currency[i]} bill'
          amount_due -= (times_how_many * currency[i])
  return holding_ground + '.'



print(optimal_change(100, 8.47))