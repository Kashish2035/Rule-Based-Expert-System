# main.py

from rules import rules
from engine import RuleEngine

print("==== Expert System (Forward Chaining) ====")

# Create engine instance
engine = RuleEngine(rules)

# Take user facts
user_input = input("Enter your symptoms (comma separated): ")
facts = [f.strip().lower().replace(" ", "_") for f in user_input.split(",")]

# Add user facts to fact base
for fact in facts:
    engine.add_fact(fact)

# Run inference
final_facts, reasoning_log = engine.forward_chain()

# Display inferred facts
print("\n--- Inferred Facts ---")
for fact in sorted(final_facts):
    print("-", fact)

# Display reasoning steps
print("\n--- Reasoning Steps ---")
if reasoning_log:
    for step in reasoning_log:
        print(step)
else:
    print("No rules matched your symptoms.")
