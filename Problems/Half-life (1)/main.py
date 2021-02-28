initial_quantity = int(input())  # atoms
final_quantity = int(input())  # quantity
half_life = 0
while initial_quantity >= final_quantity:
    initial_quantity = initial_quantity / 2
    # final_quantity = final_quantity + 1
    half_life = half_life + 12
print(int(half_life))

