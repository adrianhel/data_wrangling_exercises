# Задача №1: Количество ежедневных поездок

![Python](https://img.shields.io/badge/python-3.8-blue?logo=pypi)

### [Назад к Data Wrangling ⤶](https://github.com/adrianhel/data_wrangling_exercises/blob/main/README.md)

Сколько поездок делают каждый день клиенты системы **Citi Bike** отдельно по категориям `subscribers` и `customers`?  
Выберите один день для исследования.

## Датасет
Набор данных взят с https://s3.amazonaws.com/tripdata/index.html

Имя файла: `202009-citibike-tripdata.csv`

## Обрисовка программы
1. Считываем файл данных.  
2. Создаем переменные для подсчета значений `subscribers`, `customers` и `other`.  
3. Для каждой строки в файле:  
a) если значение `User Type` равно `Subscriber,`, инкрементируем на 1 значение `subscriber_count`;  
b) если значение `User Type` равно `Customer,`, инкрементируем на 1 значение `customer_count`;  
c) в противном случае инкрементируем на 1 значение переменной `other`.  
4. Отображаем полученные результаты.

### Код программы

[Задача №1](hitting_the_road_with_citibike.py)

## Разбор кода
### Шаг 1
Импортируем библиотеку **csv**.

```python
import csv
```

Открываем файл `202009-citibike-tripdata.csv` в режиме чтения **r**.

```python
source_file = open("202009-citibike-tripdata.csv", "r")
```

Передаем исходный файл `source_file` как аргумент методу ***DictReader*** библиотеки ***csv***.
Сохраняем результат в переменной `citibike_reader`.

```python
citibike_reader = csv.DictReader(source_file)
```

Метод ***DictReader*** добавляет в наши данные некоторую полезную информацию. Например, свойство `fieldnames` позволяет 
обращаться ко всем значениям в первой строке/заголовке.

```python
print(*citibike_reader.fieldnames, sep='\n')
```

Отображая значения `citibike_reader.fieldnames`, мы можем видеть, что точным именем столбца `User Type` является 
`usertype`.

### Шаг 2
Создаем переменные для хранения количества пользователей каждого типа.
Инициируем каждую переменную, присваивая ей значения 0.

```python
subscriber_count = 0
customer_count = 0
other_user_count = 0
```

### Шаг 3
Обрабатываем в цикле каждую строку данных

```python
for row in citibike_reader:
```

#### Шаг 3a
Если значение в столбце usertype текущей строки равно `Subscriber`

```python
    if row["usertype"] == "Subscriber":
```

инкрементируем на 1 значение переменной `subscriber_count`

```python
        subscriber_count += 1
```

#### Шаг 3b
Если значение в столбце `usertype` текущей строки равно `Customer`

```python
    elif row["usertype"] == "Customer":
```

инкрементируем на 1 значение переменной `customer_count`

```python
        customer_count += 1
```

#### Шаг 3c
Если значение в столбце `usertype` текущей строки не равно ни `Subscriber`, ни `Customer`.
Инкрементируем на 1 значение переменной `other_user_count`

```python
    else:
        other_user_count += 1
```

### Шаг 4
Отображаем результаты, включая заголовки.

Количество подписчиков

```python
print(f"Number of subscribers: {subscriber_count}")
```

Количество клиентов

```python
print(f"Number of customers: {customer_count}")
```

Количество прочих пользователей

```python
print(f"Number of 'other' users: {other_user_count}")
```

## Заключение
Посредством данного сценария мы решили следующие задачи:
1. Успешно подсчитали количество пользователей типы `Subscriber` и `Customer`,
которые использовали услуги системы **CitiBike** в сентябре 2020г.
2. Удостоверились, что столбец `usertype` не содержит никаких других типов значений, кроме этих двух, 
3. поскольку значение переменной `other_user_count` равно 0.