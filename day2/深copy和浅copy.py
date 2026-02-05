import copy

def use_copy():
    a = [1,2,[3,4]]
    b = copy.copy(a)
    b[2] = 99
    print(a)
    print(b)

if __name__ == '__main__':
    use_copy()