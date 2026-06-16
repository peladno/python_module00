def ft_count_harvest_iterative():
  days = int(input("Days until harvest: "))
  total = range(1, days + 1)
  for current_day in total:
    print(f"Day {current_day}")
  print("Harvest time!")
