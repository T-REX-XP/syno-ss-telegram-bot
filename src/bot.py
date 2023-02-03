#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import datetime
import json
import logging
import os
import sqlite3
import subprocess
import sys
import time
from sqlite3 import Error

import syno 
import telepot

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def main2(app) -> None:
    syno.run(app)
def main() -> None:
    """Start the bot."""
    token = os.environ['TELEGRAM_TOKEN']
    bot =telepot.Bot(token);
    syno.run(bot)

if __name__ == "__main__":
    main()