def find_max_reposts(num_reposts):
    repost_count = {}
    repost_count["POLYCARP"] = 1
    max_reposts = 1


    for _ in range(num_reposts):
        repost_info = input().split()
        for i in range(len(repost_info)):
            repost_info[i] = repost_info[i].upper()

        reposter = repost_info[0]
        original_poster = repost_info[-1]
        repost_count[reposter] = repost_count[original_poster] + 1
        if repost_count[reposter] > max_reposts:
            max_reposts = repost_count[reposter]

    print(max_reposts)

num_reposts = int(input())


find_max_reposts(num_reposts)