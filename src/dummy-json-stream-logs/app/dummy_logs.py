import os
import json
import time
import logging
import argparse

from pythonjsonlogger import jsonlogger

from apscheduler.schedulers.background import BackgroundScheduler


def task(name, _id):
    logger.debug(f'[task-{name}-{_id}]')


def main(name, interval=1):
    scheduler = BackgroundScheduler()
    scheduler.start()
    for i in range(10):
        scheduler.add_job(func=task, args=(name, i,),
                          id=f'task-{name}-{i}',
                          trigger='interval',
                          seconds=interval)

    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('name', type=str)
    parser.add_argument('-i', '--log-interval', type=float, default=1.0)
    args = parser.parse_args()

    # {
    #     "asctime": "2021-09-03 11:29:07,342",
    #     "levelname": "DEBUG",
    #     "name": "name",
    #     "thread": 123145683902464,
    #     "message": "[task-name-9]"
    # }

    loggingStreamHandler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter('%(asctime)s %(levelname)7s %(name)20s %(thread)d %(message)s')
    loggingStreamHandler.setFormatter(formatter)
    logger = logging.getLogger(args.name)
    logger.addHandler(loggingStreamHandler)
    logger.setLevel(logging.DEBUG)

    main(args.name, args.log_interval)
