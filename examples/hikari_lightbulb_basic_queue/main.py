import os

from consts import TOKEN, PREFIX

import hikari
import lightbulb
import lavasnek_rs


class Data:
    """Global data shared across the entire bot, used to store dashboard values."""

    def __init__(self) -> None:
        self.lavalink: lavasnek_rs.Lavalink = None


class MusicBot(lightbulb.Bot):
    """Subclass of lightbulb's Bot object, used to store the lavalink client."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = Data()


# You may want to enable ALL intents here
bot = MusicBot(token=TOKEN, prefix=PREFIX)


@bot.listen(hikari.StartingEvent)
async def starting_load_extensions(event):
    """Load the music extension when Bot starts."""
    bot.load_extension("music_plugin")


@bot.command()
async def ping(ctx):
    """Typical Ping-Pong command"""
    await ctx.respond("Ping?")


bot.run()