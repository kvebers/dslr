import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))


def check_if_can_calculate_mean(row):
    for element in row:
        if element.strip() == '':
            continue
        try:
            float(element)
        except ValueError:
            return False
    return True