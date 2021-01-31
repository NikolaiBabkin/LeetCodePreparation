def f(arr, target):
    def recursion_cal(arr, target):
        res = []
        while arr and arr[-1] >= target:
            if arr[-1] == target:
                res.append([arr.pop()])
            else:
                arr.pop()
        if arr:
            for l in recursion_cal(arr[:-1], target - arr[-1]):
                res.append(l + [arr[-1]])
        return res

    arr = sorted(arr)
    return recursion_cal(arr, target)

if __name__ == '__main__':
    arr = [1, 2, 3, 3, 6]
    target = 6
    print(f(arr, target))
