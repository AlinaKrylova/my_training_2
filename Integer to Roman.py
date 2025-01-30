# 1 способ

class Solution:
    def intToRoman(self, num: int) -> str:
        RomanNum = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        ArabNum = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numRoman = ''

        for i in range(len(RomanNum)):
            while num >= ArabNum[i]:
                numRoman += RomanNum[i]
                num -= ArabNum[i]

        return numRoman

# 2 способ

class Solution:
    def intToRoman(self, num: int) -> str:
        # Используем кортежи вместо списков
        RomanNum = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        ArabNum = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)

        # Используем список для накопления символов
        numRoman = []

        # Идем по кортежам RomanNum и ArabNum
        for i in range(len(RomanNum)):
            # Если num >= текущего значения ArabNum, добавляем RomanNum и вычитаем ArabNum
            while num >= ArabNum[i]:
                numRoman.append(RomanNum[i])
                num -= ArabNum[i]
            # Если num == 0, можно сразу завершить цикл
            if num == 0:
                break

        # Объединяем список в строку
        return ''.join(numRoman)

# 3 способ

class Solution:
    def intToRoman(self, num: int) -> str:
        # Таблицы для каждого разряда
        thousands = ['', 'M', 'MM', 'MMM']
        hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

        # Разбиваем число на разряды
        return (
                thousands[num // 1000] +  # Тысячи
                hundreds[(num % 1000) // 100] +  # Сотни
                tens[(num % 100) // 10] +  # Десятки
                ones[num % 10]  # Единицы
        )


# Проверка функции
print(Solution().intToRoman(8))  # Вывод: "VIII"
print(Solution().intToRoman(1994))  # Вывод: "MCMXCIV"
print(Solution().intToRoman(4))  # Вывод: "IV"
print(Solution().intToRoman(9))  # Вывод: "IX"