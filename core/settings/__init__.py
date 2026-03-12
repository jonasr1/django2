# ruff: noqa: F403

try:
    import MySQLdb  # noqa: F401
except ModuleNotFoundError:
    import pymysql

    pymysql.install_as_MySQLdb()

from core.settings.base import *
from core.settings.installed_apps import *
from core.settings.middlewares import *
from core.settings.pictures import *
from core.settings.storages import *
