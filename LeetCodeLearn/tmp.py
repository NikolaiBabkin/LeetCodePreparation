def f(arr):
    if len(arr) == 10:
        return True

    arr.append(1)
    f(arr)
    if f(arr):
        return True
    arr.pop()


if __name__ == '__main__':
    arr = []
    print(f(arr))
    print(arr)
