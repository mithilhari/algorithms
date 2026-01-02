def two_sum(target, arr):
    # POPULATE COMPLEMENT DICT -> (pos, complement)

    D = dict()
    k, j = None, None
    for i, val in enumerate(arr):
        if (target-val) in D:
            k = i
            j = D[target-val][0]
        else:
            D[val] = (i, target - val)

    return (j, k)
    


if __name__ == "__main__":
    x = int(input("enter a target sum "))
    arr = [7, 5, 6, 11] 
    print(two_sum(x, arr))
