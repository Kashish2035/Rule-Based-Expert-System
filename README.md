🔍 Rule-Based Inference Engine (Forward Chaining)

A lightweight rule engine that uses if–then rules and a facts base to infer conclusions using forward chaining.
This project demonstrates the fundamentals of expert systems, multi-step reasoning, and transparent inference logging.

✨ Features

User-Provided Facts
Input initial facts such as symptoms or observations.

Forward Chaining Engine
Automatically applies rules to derive new conclusions.

Multi-Step Inference (Chaining)
Supports cascading rule execution where one conclusion triggers another rule.

Reasoning Path Logging
Displays how each conclusion was reached for full transparency.

📁 Project Structure
/root
 ├── rules.json        # Define if-then rules
 ├── engine.py         # Core forward-chaining implementation
 ├── facts.py          # Facts base handler
 ├── main.py           # CLI or app entry point
 └── README.md

🚀 How It Works

Load rules and initial facts

Run forward chaining

Apply all rules whose conditions match current facts

Add new inferred facts

Continue until no new facts can be derived

Output final conclusions + reasoning log

🧪 Example Rule
{
  "if": ["fever", "cough"],
  "then": "flu"
}

Example Input Facts
fever
cough

Output
Inferred: flu  
Reason: Rule 1 fired because {fever, cough} were present.

▶️ Run the Project
python main.py

📜 License

MIT License — free to use and modify.












































 
