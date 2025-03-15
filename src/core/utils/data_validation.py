def check_if_can_calculate_mean(row):
    for element in row:
        if element.strip() == '':
            continue
        try:
            float(element)
        except ValueError:
            return False
    return True