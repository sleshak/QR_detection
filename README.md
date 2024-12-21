# Детекция QR-кода
# Оглавление
1. [Айти кошечки](#Айти-кошечки)
2. [Описание решения](#описание-решения)
3. [Техническое задание](#техническое-задание)
4. [Метрики]
5. [Как запустить](#как-запустить)

# Айти-кошечки
__Наша команда состоит из 5 человек__:
1. Витковская Полина
2. Чёо Эрика
3. Хорошко Илья
4. Рыжков Владимир
5. Каменев Александр

# Техническое задание
Для это проекта нам было необходимо:
<ol>
  <li>Собрать датасет для модели. Мы использовали как данные на облаке, так и собственно сгенерированные QR-коды.</li>
  <li>Выбрать инструменты разработки. Решили написать модель на Python, используя библиотеки pyzbar и OpenCV.</li>
  <li>Предобработать изображения. Убрать лишние цвета и отфильтровать шумы.</li>
  <li>Распознать QR-код. Определить местоположение конкретного QR-кода.</li>
  <li>Сравнить найденный QR-код с искомым.</li>
  <li>Вывести сообщение в зависимости от результата поиска.</li>
</ol>

# Описание решения
Наше решение основывается на библиотеках pyzbar и cv2

# Метрики

<table>
  <tr>
    <td>F1</td>
    <td></td>
  </tr>
  <tr>
    <td>Recall</td>
    <td></td>
  </tr>
  <tr>
    <td>Precision</td>
    <td></td>
  </tr>
</table>

# Как запустить
НИКАК
[К оглавлению](#оглавление)
