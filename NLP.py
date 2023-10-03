import spacy
from rule_reader import read_rules_from_file, display_rules

nlp = spacy.load("en_core_web_sm")

Rules = read_rules_from_file("rules.txt")

# version_to_display = input("Which version of rules would you like to see? (Version 1/Version 2): ")
# display_rules(version_to_display, Rules)

for version, rules_list in Rules.items():
    print(f"\n=== {version} ===\n")
    header = "{:<15} {:<15} {:<10} {:<10} {:<15} {:<10} {:<10} {:<10}".format(
        "Text", "Lemma", "POS", "Tag", "Dependency", "Shape", "IsAlpha", "IsStop")
    print(header)
    print('-' * len(header))
    
    for rule in rules_list:
        processed_rule = nlp(rule)
        for token in processed_rule:
            print("{:<15} {:<15} {:<10} {:<10} {:<15} {:<10} {:<10} {:<10}".format(
                token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
                token.shape_, token.is_alpha, token.is_stop))
