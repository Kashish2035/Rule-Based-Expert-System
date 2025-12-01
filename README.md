📘 Rule-Based Expert System (Forward Chaining)

A simple Rule-Based Expert System built in Python that uses forward chaining to infer conclusions from user-provided facts (symptoms).
This project demonstrates the fundamentals of knowledge-based systems, rule chaining, and inference logging.

🚀 Features

✔ Rule Engine using IF–THEN rules

✔ Forward Chaining (Data-driven reasoning)

✔ Rule Chaining (Multi-step inference)

✔ Accepts user symptoms as input

✔ Generates inferred conclusions

✔ Logs inference steps to show reasoning path

✔ Easy to extend — add more rules anytime

📂 Project Structure
project/
│── rules.py        # Knowledge base (if-then rules)
│── engine.py       # Forward chaining rule engine
│── main.py         # User interaction & inference
│── README.md       # Documentation

🧠 How It Works

User enters symptoms (facts).

The engine checks all rules.

If all conditions of a rule are satisfied, its conclusion becomes a new fact.

New facts trigger new rules → multi-step inference.

The engine stops when no more rules can be applied.

All results + reasoning steps are displayed.

📝 Example Usage
Run the program:
python main.py

Input:
fever, cough, body pain

Output:
--- Inferred Facts ---
fever
cough
body_pain
flu
viral_infection

--- Reasoning Steps ---
Rule fired: IF fever AND cough THEN flu
Rule fired: IF flu AND body_pain THEN viral_infection

🧱 Rule Base

Rules are stored in rules.py as Python dictionaries:

{
    "conditions": ["fever", "cough"],
    "conclusion": "flu"
}


Easily add more rules to expand the system.

🛠️ Installation
1. Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. Run the program
python main.py

⚙️ Requirements

Python 3.8+

No external libraries required

💡 Extending the System

You can enhance this system by adding:

✔ GUI (Tkinter / PyQt)

✔ Web App (Flask / Django)

✔ JSON or YAML rule files

✔ Medical knowledge base

✔ Cybersecurity threat detection rules

If you want, I can help you implement any of these features.

🤝 Contributing

Pull requests are welcome!
Feel free to open issues for suggestions, bugs, or improvements.

📜 License

This project is licensed under the MIT License.












































 
