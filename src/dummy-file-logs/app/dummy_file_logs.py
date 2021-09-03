import os
import time
import logging
import argparse

from apscheduler.schedulers.background import BackgroundScheduler
from logging.handlers import RotatingFileHandler


def task(name, _id):
    logger.debug(f'[task-{name}-{_id}] ')


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
    parser.add_argument('-l', '--log-path', default='./app.log')
    parser.add_argument('-i', '--log-interval', type=float, default=1.0)
    args = parser.parse_args()

    logFormatter = logging.Formatter(
        '%(asctime)s | %(levelname)7s | %(name)20s | %(thread)d | %(message)s')

    fileHandler = RotatingFileHandler(
        filename=args.log_path,
        maxBytes=(1024 * 1000) * 10,  # 10MB
        backupCount=5)
    fileHandler.setFormatter(logFormatter)
    logger = logging.getLogger(args.name)
    logger.addHandler(fileHandler)
    logger.setLevel(logging.DEBUG)

    main(args.name, args.log_interval)
