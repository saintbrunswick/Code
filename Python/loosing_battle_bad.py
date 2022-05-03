#loosing battle bad
#demostrate the infinity loop

print("Your hero is surrounded bby a massive army of trolls.")
print("Their decaying green bodies stretch out, melting in to the horizon.")
print("Your hero unsheathes his sword for the last fight of his live.\n")

health = 10
trolls = 0
damage = 3

while health > 0:
    trolls += 1
    health -= damage

    print("Your hero swings and defeats an evil troll, " \
        "but takes", damage, "damage points.\n")
print("Your hero fought valiantly and defeted", trolls, "trolls.")
print("But alas your hero is no more.")

input("\nPress enter key to exit.")