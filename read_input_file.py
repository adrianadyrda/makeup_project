def read_input():
    file = open('input.txt', encoding='utf-8')
    lines = file.readlines()
    my_list = []
    for line in lines:
        my_list.append(line.strip())
    return my_list


if __name__ == '__main__':
    print(read_input())