c1 = int(input("Player 1 - Choose your move:\n1 = Rock\n2 = Paper\n3 = Scissors\nEnter 1, 2, or 3: "))
c2 = int(input("\nPlayer 2 - Choose your move:\n1 = Rock\n2 = Paper\n3 = Scissors\nEnter 1, 2, or 3: "))

g = {1:"Rock",2:"Paper",3:"Scissors"}
for i in g:
    if c1 == i: r1 = g[i]
    if c2 == i: r2 = g[i]

if c1 >3 and c2 >3 : result = "Invalid input! Please enter 1, 2, or 3 only."
elif c1 == c2: result = "It's a tie!"
elif c1 > c2: 
    result = "Player 1 wins!"
    if c2 == 1 and c1 == 3: result = "Player 2 wins!"
elif c2 > c1: 
    result = "Player 2 wins!"
    if c1 == 1 and c2 == 3: result = "Player 1 wins!"

print(f"\nPlayer 1 chose: {r1}\nPlayer 2 chose: {r2}\n{result}")

# for i in range(stop)
# for i in range(start, stop)
# for i in range(start,stop,step):
#
# for i in name
