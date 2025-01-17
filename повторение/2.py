def main():
    try:
        n = int(input())
    except ValueError:
        print('не число')
        return
    if n < 1:
        print('не натуральное')
        return

    nums = [n]
    while True:
        if n == 1:
            break
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        nums.append(n)

    print(f"Последовательность: {'->'.join(map(str, nums))}")
    print(f"Длина: {len(nums)}")
    print(f"Пик: {max(nums)}")


if __name__ == "__main__":
    main()
