def process_test_cases():
    num_tests = int(input())
    
    for _ in range(num_tests):
        num_nodes, num_edges = map(int, input().split())
        degree_count = {i: 0 for i in range(1, num_nodes + 1)}
        
        for _ in range(num_edges):
            node1, node2 = map(int, input().split())
            degree_count[node1] += 1
            degree_count[node2] += 1

        frequency_count = {}
        for degree in degree_count.values():
            if degree not in frequency_count:
                frequency_count[degree] = 1
            else:
                frequency_count[degree] += 1

        if len(frequency_count) == 2:
            for degree in frequency_count:
                if degree != 1:
                    max_degree = degree
                    min_degree = max_degree - 1
        else:
            for degree, count in frequency_count.items():
                if count == 1:
                    max_degree = degree
            for degree, count in frequency_count.items():
                if count == max_degree:
                    min_degree = degree - 1
        
        print(max_degree, min_degree)

# Call the function to execute
process_test_cases()
