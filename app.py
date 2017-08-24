from mongoengine import *
from settings import *


def connect_db(**config_overrides):
    config = {
        'host': MONGODB_HOST,
        'port': MONGODB_PORT,
        'db': MONGODB_DB
    }

    if len(config_overrides) > 0:
        for k, v in list(config_overrides.items()):
            config[k] = v

    return connect(db=config['db'], host=config['host'], port=config['port'])


if __name__ == "__main__":
    db = connect_db(db="temp")
    print(db.name)
