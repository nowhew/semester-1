"""
GENERATE DATASET FOR DEMO
"""

import random

filepath = input()
with open(filepath, "w") as f:
    for i in range(0, 100):
        f.write(f"{random.randint(1, 1000)} ")