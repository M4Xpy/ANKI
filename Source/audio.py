def uniq_name(input_string: str, seed_sign: int = None) -> str:
    random.seed(seed_sign)
    return ''.join([char.upper() if random.random() < 0.5 else char.lower() for char in input_string[:20]])