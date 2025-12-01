# rules.py

rules = [
    # --- Common Illnesses ---
    {
        "conditions": ["fever", "cough"],
        "conclusion": "flu"
    },
    {
        "conditions": ["sore_throat", "cough"],
        "conclusion": "cold"
    },
    {
        "conditions": ["runny_nose", "sneezing"],
        "conclusion": "allergy"
    },
    {
        "conditions": ["fever", "body_pain", "weakness"],
        "conclusion": "viral_fever"
    },
    {
        "conditions": ["fever", "rash"],
        "conclusion": "measles"
    },

    # --- Multi-Step Inference (Rule Chaining) ---
    {
        "conditions": ["flu", "body_pain"],
        "conclusion": "viral_infection"
    },
    {
        "conditions": ["cold", "fever"],
        "conclusion": "throat_infection"
    },

    # --- Stomach Related ---
    {
        "conditions": ["stomach_pain", "vomiting"],
        "conclusion": "food_poisoning"
    },
    {
        "conditions": ["nausea", "headache"],
        "conclusion": "migraine"
    },

    # --- Serious Illnesses ---
    {
        "conditions": ["chest_pain", "shortness_of_breath"],
        "conclusion": "heart_issue"
    },
    {
        "conditions": ["fever", "headache", "neck_stiffness"],
        "conclusion": "meningitis"
    },
    {
        "conditions": ["high_fever", "joint_pain", "rash"],
        "conclusion": "dengue"
    },

    # --- Covid Related ---
    {
        "conditions": ["fever", "loss_of_smell", "cough"],
        "conclusion": "covid_suspected"
    },

    # --- Pneumonia ---
    {
        "conditions": ["fever", "chills", "cough", "breathing_difficulty"],
        "conclusion": "pneumonia"
    },

    # --- Typhoid ---
    {
        "conditions": ["fever", "abdominal_pain", "weakness"],
        "conclusion": "typhoid"
    },

    # --- Malaria ---
    {
        "conditions": ["fever", "chills", "sweating"],
        "conclusion": "malaria"
    }
]
