import logging
import tzlocal
from datetime import datetime
from colorlog import ColoredFormatter


def posix2local(timestamp, tz=tzlocal.get_localzone()):
    """Seconds since the epoch -> local time as an aware datetime object."""
    return datetime.fromtimestamp(timestamp, tz)


class Formatter(ColoredFormatter):
    def converter(self, timestamp):
        return posix2local(timestamp)

    def formatTime(self, record, datefmt=None):
        dt = self.converter(record.created)
        if datefmt:
            s = dt.strftime(datefmt)
        else:
            t = dt.strftime(self.default_time_format)
            s = self.default_msec_format % (t, record.msecs)
        return s


_LOGGER = logging.getLogger(__name__)

fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
colorfmt = '%(log_color)s{}%(reset)s'.format(fmt)
datefmt = '%Y-%m-%dT%H:%M:%S%z'
logging.basicConfig(level=logging.DEBUG)
logging.getLogger().handlers[0].setFormatter(Formatter(
    colorfmt,
    datefmt=datefmt,
    reset=True,
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red',

    }
))

config = {}


def get_config():
    _LOGGER.debug('Have some configs.')
    return config
