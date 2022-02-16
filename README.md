# Эффективная быстрая сортировка.
Отличие от обычного алгоритма быстрой сортировки в том, что не происходит использования дополнительной памяти.

## Описание

На соревнованиях по спортивному программированию каждый участник имеет уникальный логин. Когда соревнование закончится, к нему будут привязаны два показателя: количество решённых задач Pi и размер штрафа Fi. Штраф начисляется за неудачные попытки и время, затраченное на задачу.

Принято решение сортировать таблицу результатов следующим образом: при сравнении двух участников выше будет идти тот, у которого решено больше задач. При равенстве числа решённых задач первым идёт участник с меньшим штрафом. Если же и штрафы совпадают, то первым будет тот, у которого логин идёт раньше в алфавитном (лексикографическом) порядке.

Реализация сортировки не может потреблять О(n) дополнительной памяти для промежуточных данных (такая модификация быстрой сортировки называется "in-place").

## Пример 1
Input:
```
$ python ./main.py
5
alla 4 100
gena 6 1000
gosha 2 90
rita 2 90
timofey 4 80
```
Output:
```
gena
timofey
alla
gosha
rita
```

## Пример 2
Input:
```
$ python ./main.py
5
alla 0 0
gena 0 0
gosha 0 0
rita 0 0
timofey 0 0
```
Output:
```
alla
gena
gosha
rita
timofey
```


## Зависимости
1. Python >= 3.9

## Автор
Солилов Александр