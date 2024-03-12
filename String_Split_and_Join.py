def split_and_join(line):
    # write your code here

    words = line.split(" ")

    # Join the words with hyphens
    joined_string = "-".join(words)

    return joined_string

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)