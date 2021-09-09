import os
import time
import logging
import argparse
import random
import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from logging.handlers import RotatingFileHandler
from pythonjsonlogger import jsonlogger


def task(name, _id):
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    t1 = f'user {{"reg_date": "{dt}", "log_type": 801, "account_id": 0, "user_name": "aaaa", "player_id": 1, "room_uid": "20210907175052001"}}'
    t2 = f'game {{"reg_date": "{dt}", "log_type": 1001, "room_uid": "20210907171213001", "match_type": 0, "game_mode": 1}}'
    logs = [t1, t2]
    log = random.choice(logs)
    logger.debug(log)


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

    fileHandler = RotatingFileHandler(
        filename=args.log_path,
        maxBytes=(1024 * 1000) * 10,  # 10MB
        backupCount=5)

    logger = logging.getLogger(args.name)
    logger.addHandler(fileHandler)
    logger.setLevel(logging.DEBUG)

    main(args.name, args.log_interval)
