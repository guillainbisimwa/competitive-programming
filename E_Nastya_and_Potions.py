from collections import defaultdict, deque

def potion_mixing_simulation():
    test_cases = int(input())
    results_list = []

    for case in range(test_cases):
        num_potions, num_available = map(int, input().split())
        potion_costs = list(map(int, input().split()))
        final_costs = [0] * num_potions
        available_potions = set(int(x) - 1 for x in input().split())
        dependency_graph = defaultdict(list)
        processing_queue = deque()
        dependency_counts = [0] * num_potions

        for potion_index in range(num_potions):
            mixing_dependencies = map(int, input().split())
            if next(mixing_dependencies) == 0:
                processing_queue.append(potion_index)
                final_costs[potion_index] = potion_costs[potion_index]
            else:
                for dependency in mixing_dependencies:
                    dependency_graph[dependency - 1].append(potion_index)
                    dependency_counts[potion_index] += 1

        while processing_queue:
            current_potion = processing_queue.popleft()
            if current_potion in available_potions:
                final_costs[current_potion] = 0
            else:
                final_costs[current_potion] = min(potion_costs[current_potion], final_costs[current_potion])

            for dependent_potion in dependency_graph[current_potion]:
                dependency_counts[dependent_potion] -= 1
                final_costs[dependent_potion] += final_costs[current_potion]
                if dependency_counts[dependent_potion] == 0:
                    processing_queue.append(dependent_potion)

        results_list.append(" ".join(map(str, final_costs)))

    print("\n".join(results_list))

# Run the function
potion_mixing_simulation()
