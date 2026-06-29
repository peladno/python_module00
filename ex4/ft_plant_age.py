def ft_plant_age():
    ready_to_harvest_day = 60
    age = int(input("Enter plant age in days: "))
    if age > ready_to_harvest_day:
        print("Plant is ready to harvest!")
    else:
        print("Plants needs more time to grow.")
