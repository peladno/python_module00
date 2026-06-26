def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def _count(current_day: int, total: int):
        if current_day > total:
            print("Harvest time!")
            return
        print(f"Day {current_day}")
        _count(current_day + 1, total)

    _count(1, days)
