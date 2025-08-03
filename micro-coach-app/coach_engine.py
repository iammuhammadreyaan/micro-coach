# coach_engine.py

import random

advice_bank = {
    "sleep": [
        "Start winding down 30 minutes before bed — avoid screens.",
        "Wake up at the same time daily — even on weekends.",
        "Use light: sunlight in the morning, darkness at night.",
    ],
    "focus": [
        "Use the Pomodoro technique: 25 min work, 5 min break.",
        "Clear your physical space to clear your mental space.",
        "Start with the smallest task to build momentum.",
    ],
    "fitness": [
        "Lay out your clothes before bed — remove decision friction.",
        "Don’t aim for perfection — aim for consistency.",
        "Exercise at the same time daily to create rhythm.",
    ],
    "motivation": [
        "You don’t need motivation — you need a system.",
        "Lower the bar — doing something is better than nothing.",
        "Visualize your future self thanking you.",
    ],
    "reading": [
        "Always carry a book — even if it’s digital.",
        "Set a 5-minute reading timer — it usually turns into more.",
        "Associate reading with a daily cue (tea, bedtime, commute).",
    ],
    "default": [
        "Progress beats perfection. Always.",
        "Your environment shapes your habits. Adjust it.",
        "Make it obvious. Make it easy. Make it satisfying.",
    ]
}

def get_advice(user_input):
    input_lower = user_input.lower()
    for topic, tips in advice_bank.items():
        if topic in input_lower:
            return random.choice(tips)
    return random.choice(advice_bank["default"])