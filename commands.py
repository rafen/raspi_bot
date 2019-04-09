from datetime import datetime

import RPi.GPIO as GPIO
from decorators import private, time_sensitive

GPIO.setmode(GPIO.BMC)
# light output pin
light_pin = 16
GPIO.setup(light_pin, GPIO.OUT)
GPIO.output(light_pin, GPIO.LOW)


def start(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="I'm a bot, please say hi!"
    )


def hi(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Hi! {} ({})".format(
            update.message.from_user.first_name,
            update.message.from_user.id
        )
    )


def thanks(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Thank you! {} ({})".format(
            update.message.from_user.first_name,
            update.message.from_user.id
        )
    )


@private
@time_sensitive
def time(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="my time is {}".format(datetime.now())
    )


@private
@time_sensitive
def light_on(bot, update):
    GPIO.output(light_pin, GPIO.HIGH)
    bot.send_message(
        chat_id=update.message.chat_id,
        text="light is on now"
    )


@private
@time_sensitive
def light_off(bot, update):
    GPIO.output(light_pin, GPIO.LOW)
    bot.send_message(
        chat_id=update.message.chat_id,
        text="light is off"
    )


command_list = [
    # list of command to expose
    # name, function
    ('start', start),
    ('hi', hi),
    ('thanks', thanks),
    ('time', time),
    ('on', light_on),
    ('off', light_off),
]
