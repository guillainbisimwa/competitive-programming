def split_and_join(line):
    newString = line.split(" ")
    result = '-'.join(newString)
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)