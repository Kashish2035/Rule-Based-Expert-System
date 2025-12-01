# engine.py

class RuleEngine:
    def __init__(self, rules):
        self.rules = rules
        self.facts = set()
        self.log = []

    def add_fact(self, fact):
        self.facts.add(fact)

    def forward_chain(self):
        added_new_fact = True

        while added_new_fact:
            added_new_fact = False

            for rule in self.rules:
                if all(cond in self.facts for cond in rule["conditions"]):

                    conclusion = rule["conclusion"]

                    if conclusion not in self.facts:
                        self.facts.add(conclusion)
                        added_new_fact = True

                        self.log.append(
                            f"Rule fired: IF {' AND '.join(rule['conditions'])} THEN {conclusion}"
                        )

        return self.facts, self.log
