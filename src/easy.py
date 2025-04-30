#longest-common-prefix. Бинарный поиск вместо прохода по всем символам строки
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        # Минимальная длина строки
        min_len = min(len(s) for s in strs)
        left, right = 0, min_len

        while left < right:
            mid = (left + right + 1) // 2
            prefix = strs[0][:mid]

            if all(s.startswith(prefix) for s in strs):
                left = mid
            else:
                right = mid - 1

        return strs[0][:left]
        
#palindrome. Реверс строки вмсето попарного сравнения 
def is_palindrome(s):
    # Приводим строку к нижнему регистру и убираем пробелы
    s = s.lower().replace(" ", "")
    # Проверяем равенство строки и её реверса
    return s == s[::-1]

#two_sum. Использование словаря(хэш таблицы) вместо обхода всех пар
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


    
