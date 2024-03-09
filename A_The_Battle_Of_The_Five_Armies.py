def battle_of_five_armies(soldiers_damage, soldier_count):
 
  # Extract damage and soldier count for each alliance

  A = soldiers_damage[0] * soldier_count[0]
  B = soldiers_damage[1] * soldier_count[1]
  C = soldiers_damage[2] * soldier_count[2]
  D = soldiers_damage[3] * soldier_count[3]
  E = soldiers_damage[4] * soldier_count[4]

  # Calculate total power for each side
  allies_power = A+B+C
  enemies_power = D+E

  # Determine the outcome
  if allies_power > enemies_power:
    return "WIN"
  elif allies_power < enemies_power:
    return "LOSE"
  else:
    return "DRAW"

damage_per_soldier = list(map(int, input().split()))
soldiers_count = list(map(int, input().split()))

print(battle_of_five_armies(damage_per_soldier, soldiers_count))
