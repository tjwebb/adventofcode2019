# part 1
total_fuel = 0
f = open('day1_input.txt')
for mass in f.readlines():
    fuel = (int(mass) // 3) - 2
    total_fuel = total_fuel + fuel

print('total fuel', total_fuel)

# part 2
def calc_fuel (module_mass, total_mass, fuel_mass):
    fuel_mass = (fuel_mass // 3) - 2

    if fuel_mass <= 0:
        return total_mass - module_mass

    return calc_fuel(module_mass, total_mass + fuel_mass, fuel_mass)

total_fuel = 0
f = open('day1_input.txt')
for mass in f.readlines():
    fuel = calc_fuel(int(mass), int(mass), int(mass))
    total_fuel = total_fuel + fuel

print('total fuel', total_fuel)
