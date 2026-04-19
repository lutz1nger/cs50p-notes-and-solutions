def main():
    mass = int(input('mass:'))
    print(energy_to_mass(mass))

def energy_to_mass(mass):
    return mass*300000000**2

main()
