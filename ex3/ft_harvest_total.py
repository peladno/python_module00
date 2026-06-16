def ft_harvest_total():
  day = 1
  total_harvest = 0
  while day < 4:
    total_harvest += int(input(f"Day {day} harvest: "))
    day += 1
    
  print(f"Total harvest: {total_harvest}")