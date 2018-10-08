# VK Music Downloader
Проект предназначен для использования в социальной сети [ВКонтакте](https://vk.com).

Позволяет:
1. Скачивать аудиозаписи средствами браузера из списка аудиозаписей пользователя, либо из плейлиста.
2. Сохранить список отмеченных выше аудиозаписей в файл и сохранить его на компьютере. В файле будет список из исполнителя и названия песни и URL, по которому находится mp3 файл песни. Песня и её URL разделены знаком [табуляции](https://ru.wikipedia.org/wiki/Табуляция) – `\t`. (Однако вк динамически создаёт URL при воспроизведении аудио, поэтому найти файл по этому адресу можно будет только в течении ограниченного времени. Потом Вы получите [404](https://ru.wikipedia.org/wiki/HTTP_404)).
3. Загрузить аудиозаписи, сохранённые в файл средствами скрипта на языке `python3`. Для этого на компьютере должен быть установлен интерпретатор python.

## Инструкция
### 1. Установка
Если Вы хотите скачать аудиозаписи можете пропустить этот пункт.
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
   git clone https://github.com/artslob/VkMusicDownloader.git
   cd VkMusicDownloader
   python3 -m venv vk_venv
   source vk_venv/bin/activate
   
   # windows
   git clone https://github.com/artslob/VkMusicDownloader.git
   cd VkMusicDownloader
   python3 -m venv vk_venv
   vk_venv\Scripts\activate.bat
   ```
### 2. Использование
TODO

## Лицензия
[MIT License](LICENSE.txt)