def optimal_change(item_cost, amount_paid):
  
#Create dictionary of currency:denomination
#variable called amount due that holds value of amount paid - item cost

  currency = [100,50,20,10,5,1]
  denomination = ['Hundred', 'Fifty', 'Twenty', 'Ten', 'Five,', 'One']

  amount_due = amount_paid - item_cost

  while amount_due > 0:
    for i in range(len(currency)):
      if (amount_due >= currency[i]):
        print(currency[i], amount_due)
        number_of_times = amount_due // currency[i]
        denominationhowmanytimes = denomination[i]
        currencytimes = number_of_times * denominationhowmanytimes
        amount_due -= currency[i]
        print(currency[i], amount_due, number_of_times, denominationhowmanytimes, currencytimes)


print(optimal_change(10, 30))