def calculate_powers(a, b, m):
 
  power = pow(a, b)
  print(power)

  if m is not None:
    modulo_power = pow(a, b, m)
    print(modulo_power)

# # Get input from the user
a = int(input())
b = int(input())
m = int(input())

# Calculate and print the powers
calculate_powers(3, 4, 5)
