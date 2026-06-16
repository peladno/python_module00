def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type_cap = seed_type.capitalize()
    result = "Unknown unit type"

    if unit == "packets":
        result = f"{seed_type_cap} seeds: {quantity} {unit} available"
    elif unit == "grams":
        result = f"{seed_type_cap} seeds: {quantity} {unit} total"
    elif unit == "area":
        result = f"{seed_type_cap} seeds: covers {quantity} square meters"

    print(result)
