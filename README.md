# How to dockerize your Telegram bot

Clone or fork this repo to use it as a base to create a dockerized  Telegram bot, using Python as programming language.

## Structure

* `bot.py`: your bot's codebase
* `Dockerfile`: the file to build the bot image.
* `docker-compose.yml`: used to start the bot.
* `requirements.txt`: used to specify your dependencies.

## How to deploy the bot

1. Clone or fork this repo.
3. Write an `.env` file with your `TELEGRAM_TOKEN` in it and other env vars.
4. Run `docker-compose up -d` and wait for the build to finish.

That's it. Enjoy your dockerized bot. 🚀


Config synology cameras camera example:

```
   {
     "id": 3,
     "name": "panels",
     "skip_first_n_secs": 0,
     "max_length_secs": 10,
     "scale": 1280
   }
```
