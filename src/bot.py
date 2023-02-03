#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# This program is dedicated to the public domain under the CC0 license.

import logging
import os

import syno 
import telepot

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

def main() -> None:
    """Start the bot."""
    token = os.environ['TELEGRAM_TOKEN']
    bot =telepot.Bot(token)
    syno.run(bot)

if __name__ == "__main__":
    main()