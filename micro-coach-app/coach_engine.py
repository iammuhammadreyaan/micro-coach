# coach_engine.py

import random

def get_advice():
    advice_list = [
        "Take a deep breath and keep going.",
        "Focus on what you can control.",
        "Small steps are better than no steps.",
        "You're capable of more than you think.",
        "Discomfort means you're growing.",
        "Clarity comes from action, not thought.",
        "Trust your intuition — it’s powerful.",
        "Every day is a fresh start."
    ]
    return random.choice(advice_list)
