def find_indices(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
    
def test_1():
    result = find_indices([2, 7, 11, 15], 9)
    print(f"Тест 1: {result}")
    assert result == [0, 1], f"Ожидалось [0, 1], получили {result}"

def test_2():
    result = find_indices([3, 2, 4], 6)
    print(f"Тест 2: {result}")
    assert result == [1, 2], f"Ожидалось [1, 2], получили {result}"

def test_3():
    result = find_indices([3, 3], 6)
    print(f"Тест 3: {result}")
    assert result == [0, 1], f"Ожидалось [0, 1], получили {result}"

test_1()
test_2()
test_3()
    
print("Все тесты прошли успешно!")
