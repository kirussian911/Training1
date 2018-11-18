"Найти 3 самых популярных слова"
1234
import operator

# создадим переменную, в которую положим вывод this

zen = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

# Разбиваем нашу большую строку на слова
# Создадим переменную zen_map, в которой будем хранить кол-во слов, которые мы уже нашли
zen_map = dict()

for word in zen.split():
    cleaned_word = word.strip('.,-!*').lower()
# Теперь проверяем слово на наличии в zen_map, где 0 - это слово мы не встречали, 1 - встречали
    if cleaned_word not in zen_map:
        zen_map[cleaned_word] = 0
    zen_map[cleaned_word] += 1

# Теперь нам нужно красиво вывести, какие слова встречаются чаще всего
# Нужно упорядочить словарь через items и это будет список tuple

zen_items = zen_map.items()

# Сортируем не по ключу, а по значению через модуль operator
word_count_items = sorted(
    zen_items, key=operator.itemgetter(1), reverse=True
)

print(word_count_items[:5])
