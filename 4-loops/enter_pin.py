# Enter PIN 🏦
# Codédex

print("BANK OF CODÉDEX")

pin = int(input("Enter your PIN: "))

while pin != 1234:
  #added the int cast for the new input
  pin = int(input("Incorrect PIN. Enter your PIN again: "))

  if pin == 1234:
    print("PIN accepted!")
