# Ресайзилка изображений
Меняет размер изображения согласно переданным аргументам

## ## Инструкции
Для запуска нужно запустить консоль/терминал и выполнить:

```
python3 image_resize.py source --w --h --s --o
```

**где:**
source - путь к картинке вместе с её расширением 
*(можно указать только название изображения, если оно находиться в папке со скриптом)*

--w (--width) - желаемая ширина картинки
*(если указана только ширина, высота рассчитывается автоматический в соответствий с пропорцией)*

--h (--height) - желаемая высота картинки
*(если указана только высота, ширина рассчитывается автоматический в соответствий с пропорцией)*

--s (--scale) - желаемый масштаб изображения

--o (--output) - путь вывода изображения
