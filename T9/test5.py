def is_perfect_square(n):
    if n < 0:          # Исправлено условие для n = 0
        return False
    if n == 0 or n == 1:  # Добавлена проверка для n = 0
        return True

    low = 2
    high = n // 2       # Исправлено: high = n // 2

    while low <= high:
        mid = (low + high) // 2
        mid_sq = mid * mid

        if mid_sq == n:
            return True
        elif mid_sq < n:
            low = mid + 1
        else:
            high = mid - 1

    return False
