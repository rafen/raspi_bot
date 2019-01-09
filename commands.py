from datetime import datetime

from decorators import private, time_sensitive


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


command_list = [
    # list of command to expose
    # name, function
    ('start', start),
    ('hi', hi),
    ('thanks', thanks),
    ('time', time),
]
