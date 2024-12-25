import sys

def main():
    n, num_rivalries, experts, rivalries = parse_input()
    best_team = largest_valid(n, experts, rivalries)
    res(best_team)

def parse_input():
    input = sys.stdin.read
    lines = input().strip().splitlines()
    
    n, num_rivalries = map(int, lines[0].split())
    experts = [lines[i] for i in range(1, n + 1)]
    rivalries = set(tuple(lines[j].split()) for j in range(n + 1, n + 1 + num_rivalries))
    
    return n, num_rivalries, experts, rivalries

def valid_team(subset, riv):
    subset_set = set(subset)
    for a, b in riv:
        if a in subset_set and b in subset_set:
            return False
    return True

def largest_valid(n, experts, riv):
    best_team = []
    
    for mask in range(1, 1 << n):
        current_team = [experts[j] for j in range(n) if mask & (1 << j)]
        if valid_team(current_team, riv) and len(current_team) > len(best_team):
            best_team = current_team
    
    return best_team

def res(team):
    print(len(team))
    for name in sorted(team):
        print(name)

if __name__ == "__main__":
    main()
