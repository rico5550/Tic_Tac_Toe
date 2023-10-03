def read_rules_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    rules = {}
    key = None
    for line in lines:
        line = line.strip()
        if line.startswith("Version"):
            key = line
            rules[key] = []
        elif line:  # This ensures we don't consider empty lines
            rules[key].append(line)

    return rules


def display_rules(version, rules):
    for idx, rule in enumerate(rules[version], 1):
        print(f"{idx}. {rule}")

