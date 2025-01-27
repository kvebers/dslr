def value_in_features(value: str, features:list ) -> bool:
    for item in features:
        if item:
            value == item.get("Hogwarts House")
            return True
    return False


def extract_features(values: list[dict]) -> list[list[dict]]:
    features = []
    for value in values:
        house = value.get("Hogwarts House")
        if value_in_features(house, features) == False:
            feat = []
            feat.append(value)
            features.append(feat)
        else: 
            for i in range(0, len(features:)
                if feat.get("Hogwarts House") == house:




def execute_describe(values: list[dict]):
