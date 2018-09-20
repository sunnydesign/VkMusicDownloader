import argparse
import asyncio
import logging
import os
import sys
from argparse import FileType
from logging import FileHandler
from os.path import join

import aiofiles
import aiohttp

logger: logging.Logger

LogLevels = {
    0: logging.WARNING,
    1: logging.INFO,
    2: logging.DEBUG,
}


def get_parser():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parser = argparse.ArgumentParser(description='Download audios from text file with links.')
    parser.add_argument('-d', '--dir', dest='dir', type=str, default=current_dir,
                        help='Destination directory where audios are saved. Default: %(default)s.')
    parser.add_argument('-f', '--file', dest='file', type=FileType(), default=join(current_dir, 'audios.txt'),
                        help="File that contains names of songs and their urls. Can be set to stdin with value '-'. "
                             "Default: %(default)s.")
    parser.add_argument('-n', '--number', dest='number', type=int, default=10,
                        help='Number of files that downloading at the same time. Default: %(default)s.')
    parser.add_argument('-l', '--logfile', dest='logfile', type=FileType('w'), default='-',
                        help="Writable file for logging. By default set to stdout with value '%(default)s'.")
    parser.add_argument('-v', '--verbose', dest='verbose', default=0, action='count',
                        help='Set level of logging. You can increase level by repeating key. Levels by number: ' +
                             ', '.join(f'{"-" + "v" * number if number else "default"}: {logging._levelToName[level]}'
                                       for number, level in LogLevels.items()))
    return parser


def get_logger(args, program_name):
    logging_params = {
        'format': '[%(asctime)s] [%(levelname)s] %(message)s',
        'datefmt': '%H:%M:%S',
    }

    if args.logfile is not sys.stdout:
        logging_params['handlers'] = [FileHandler(args.logfile.name, encoding='utf8'), ]

    for number, level in LogLevels.items():
        if number == args.number:
            logging_params['level'] = level
            break
    else:
        logging_params['level'] = LogLevels[0]

    logging.basicConfig(**logging_params)

    return logging.getLogger(program_name)


async def download_coroutine(session, name, url, chunk_size=1 << 15):
    try:
        async with session.get(url) as response:
            logging.info('downloading %s', name)
            filename = os.path.join('/E/Music/vk/', name)  # TODO: change for args.dir
            async with aiofiles.open(filename, 'wb') as file:
                while True:
                    chunk = await response.content.read(chunk_size)
                    if not chunk:
                        break
                    await file.write(chunk)
            logging.info('done %s', name)
            return await response.release()
    except aiohttp.client_exceptions.ClientError as e:
        logging.exception('error occurred')


async def download(loop, name, url):
    async with aiohttp.ClientSession(loop=loop) as session:
        await download_coroutine(session, name, url)


def main():
    global logger

    parser = get_parser()
    args = parser.parse_args()
    logger = get_logger(args, parser.prog)

    data = []
    for line in args.file.readlines():
        name, url = (el.strip() for el in line.strip().split('\t'))
        name: str
        data.append((name.replace('/', ''), url))

    num = args.number

    loop = asyncio.get_event_loop()
    for i in range(len(data) // num):
        low, upper = i * num, (i + 1) * num
        loop.run_until_complete(asyncio.gather(*(download(loop, name, url) for name, url in data[low:upper])))


if __name__ == '__main__':
    main()
