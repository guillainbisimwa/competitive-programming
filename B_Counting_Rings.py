def count_rings(sequence):

  consecutive_rings = 0
  max_rings = 0

  for char in sequence:
    if char != "O":
      consecutive_rings = 0
    else:
      consecutive_rings += 1
      max_rings = max(max_rings, consecutive_rings)

  return max_rings

sequence = input()
print(count_rings(sequence))
