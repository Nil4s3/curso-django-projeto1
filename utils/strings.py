

def is_positive_number(value):
    try:
        number_sting = float(value)
    except ValueError:
        return False

    return number_sting > 0
