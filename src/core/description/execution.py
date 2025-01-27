from pprint import pprint

def value_in_features(value: str, features:list ) -> bool:
    if features == []:
        False
    for i in range(0, len(features)):
        if features[i]:
            if value == features[i][0].get("Hogwarts House"):
                return True
    return False

def match_features(value: str, features:list):
    for i in range(0, len(features)):
        if features[i][0]:
            if value == features[i][0].get("Hogwarts House"):
                return i
    return -1


def extract_features(values: list[dict]) -> list[list[dict]]:
    features = []
    for j in range(0, len(values)):
        house = values[j].get("Hogwarts House")
        if value_in_features(house, features) == False:
            feat = []
            feat.append(values[j])
            features.append(feat)
        else: 
            index = match_features(house, features)
            features[index].append(values[j])
    return features

def execute_calculation(features:list):
    keys_list = list(features[0].keys())
    result = []
    for i in range(1,len(keys_list)):
        numbers = []
        for value in features:
            try:
                flo = float(value.get(keys_list[i]))
                numbers.append(flo)
            except:
                continue
            try: 
                num = int(value.get(keys_list[i]))
                numbers.append(num)
            except:
                continue
        if numbers:
            numbers.insert(0,keys_list[i])
            result.append(numbers)
    print(result[0][0])
    # count(numbers)
    # calculate_mean(numbers)
    # calculate_min(numbers)
    # calculate_twentyfive(numbers)
    # calculate_fifty(numbers)
    # calculate_seventyfive(numbers)
    # calculate_max(numbers)









                   
        


def execute_describe(values: list[dict]):
    features = extract_features(values)
    result = []
    for i in range(0, len(features)):
        result = execute_calculation(features[i])

    pass