import random


diceArt = { 
1:(
"┏────────────────┐",
"│                │",
"│                │",
"│       ●        │",
"│                │",
"│                │",
"└────────────────┘"),
    2:(
"┏────────────────┐",
"│                │",
"│                │",
"│    ●       ●   │",
"│                │",
"│                │",
"└────────────────┘",
    ),
3: (
    "┏─────────────────┐",
    "│  ●              │",
    "│                 │",
    "│       ●         │",
    "│                 │",
    "│             ●   │",
    "└─────────────────┘",
),
4:(
    "┏────────────────┐",
    "│  ●         ●   │",
    "│                │",
    "│                │",
    "│                │",
    "│  ●         ●   │",
    "└────────────────┘",
),
5:(
    "┏────────────────┐",
    "│  ●         ●   │",
    "│                │",
    "│       ●        │",
    "│                │",
    "│  ●         ●   │",
    "└────────────────┘",
    ),
6: (
    "┏────────────────┐",
    "│  ●    ●     ●  │",
    "│                │",
    "│                │",
    "│                │",
    "│  ●    ●     ●  │",
    "└────────────────┘",
)
}
dice = []
total= 0
numDice = int(input("how many dice ?"))
for die in range(numDice):
    dice.append(random.randint(1, 6))

# for die in range(numDice):
#     for line in diceArt.get(dice[die]):
#         print(line)
        
for line in range(7):
    for die in dice:
        print(diceArt.get(die)[line], end="")
    print()
    
    
for die in dice:
    total += die
    
    print(f"DICE ARE: {die}")
print(f"TOTAL OF DICE IS: {total}")