# -*- coding: utf-8 -*-
import random # Добавляем модуль рандом, который позволит нам выбрать рандомное число/слово/объект из предложенных
from colorama import Fore, Back, Style # Добавляем модуль для окраски текста

answers = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да", "Можешь быть уверен в этом", "Мне кажется — «да»", "Вероятнее всего",
 "Хорошие перспективы", "Знаки говорят — «да»", "Да", "Пока не ясно, попробуй снова", "Спроси позже", "Лучше не рассказывать",
  "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ — «нет»", "По моим данным — «нет»",
   "Перспективы не очень хорошие", "Весьма сомнительно"] # Массив в котором будут наши ответы шара
print(Fore.RED + "Это шар предсказаний") # Приветствие
print(Fore.GREEN + "Напишите свой вопрос ниже") # Просьба задать вопрос
input("Вопрос: ") # Функция для того чтобы пользователь мог написать вопрос
baba = random.choice(answers) # Выбираем случайное из массива с ответами и записываем в переменную "baba"
if baba == "Бесспорно" or baba == "Предрешено" or baba == "Никаких сомнений" or baba == "Определённо да" or baba == "Можешь быть уверен в этом": # Если один из этих ответов, то цвет синий
	print(Fore.BLUE + baba)
elif baba == "Мне кажется — «да»" or baba == "Вероятнее всего" or baba == "Хорошие перспективы" or baba == "Знаки говорят — «да»" or baba == "Да": # Если один из этих ответов, то цвет зеленый
	print(Fore.GREEN + baba)
elif baba == "Пока не ясно, попробуй снова" or baba == "Спроси позже" or baba == "Лучше не рассказывать" or baba == "Сейчас нельзя предсказать" or baba == "Сконцентрируйся и спроси опять": # Если один из этих ответов, то цвет желтый
	print(Fore.YELLOW + baba)
elif baba == "Даже не думай" or baba == "Мой ответ — «нет»" or baba == "По моим данным — «нет»" or baba == "Перспективы не очень хорошие" or baba == "Весьма сомнительно": # Если один из этих ответов, то цвет красный
	print(Fore.RED + baba)
else: # Иначе, пишем просто ответ
	print(baba)
input("Нажмите любую клавишу, чтобы выйти...") # Функция печати для того чтобы программа сразу не завершилась.
