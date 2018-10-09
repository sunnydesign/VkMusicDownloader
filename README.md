# VK Music Downloader
Проект предназначен для использования в социальной сети [ВКонтакте](https://vk.com).

Позволяет:
1. Скачивать аудиозаписи средствами браузера из списка аудиозаписей пользователя, либо из плейлиста.
2. Сохранить список отмеченных выше аудиозаписей в файл и сохранить его на компьютере. В файле будет список из исполнителя и названия песни и URL, по которому находится mp3 файл песни. Песня и её URL разделены знаком [табуляции](https://ru.wikipedia.org/wiki/Табуляция) – `\t`. (Однако вк динамически создаёт URL при воспроизведении аудио, поэтому найти файл по этому адресу можно будет только в течении ограниченного времени. Потом Вы получите [404](https://ru.wikipedia.org/wiki/HTTP_404)).
3. Загрузить аудиозаписи, сохранённые в файл средствами скрипта на языке `python3`. Для этого на компьютере должен быть установлен интерпретатор python.

## Инструкция
### 1. Установка
Если Вы хотите просто скачать аудиозаписи средствами браузера или сохранить список аудиозаписей как текстовый файл, можете пропустить этот пункт.
1. Скачайте исходный код проекта. Это можно сделать 2 способами:  
   * Скачайте и разархивируйте [zip-архив](../../archive/master.zip).
   * Либо используйте git:
   ```
   git clone https://github.com/artslob/VkMusicDownloader.git
   ```
2. Если Вы будете использовать питоновский скрипт:

   Убедитесь, что у Вас есть интерпретатор python3 и он доступен из командной строки:
   ```bash
   # linux
   which python3
   
   # windows
   where python3
   ```
   Затем установим виртуальное окружение:
   ```bash
   # unix
   cd VkMusicDownloader
   python3 -m venv vk_venv
   source vk_venv/bin/activate
   
   # windows
   cd VkMusicDownloader
   python3 -m venv vk_venv
   vk_venv\Scripts\activate.bat
   ```
### 2. Использование
#### 2.1 Загрузка аудиозаписей средствами браузера
1. Открываем содержимое файла [vk-audio-downloader.js](../../raw/master/vk-audio-downloader.js). Выделяем весь текст (`Ctrl+A`) и копируем (`Ctrl+C`).
1. Заходим в раздел с аудиозаписями.
1. Листаем в самый низ. (Чтобы прогрузились все аудиозаписи) (Можно зажать клавишу PageDown)
1. Открываем консоль браузера. (`F12` -> Консоль либо `Ctrl+Shift+J`)
1. Вставляем код.
1. Пролистайте в самый верх вставленного Вами кода. Найдите строку: `var VK_DOWNLOADER_HANDLER_TYPE = 'TEXT';`. Замените `TEXT` на `FILE`. Должно получиться `var VK_DOWNLOADER_HANDLER_TYPE = 'FILE';`.
1. Если хотите загрузить только N первых (недавно добавленных) аудиозаписей, то найдите строку `var VK_DOWNLOADER_DOWNLOAD_LATEST = 0;`. Замените `0` на нужное число. Например: `var VK_DOWNLOADER_DOWNLOAD_LATEST = 50;`, тогда загрузятся только 50 первых в списке аудиозаписей.
1. Нажмите Enter. Скачивание началось...
1. Браузер может потребовать разрешение на сохранение файлов, необходимо подтвердить действие.
1. Оставляем браузер на время прямо пропорциональное количеству аудиозаписей. В консоли будет отображаться прогресс скачивания.

## Лицензия
[MIT License](LICENSE.txt)
