from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", 2a87af806641e62069aac6fb658675d6")
      API_ID = int(getenv("API_ID", 23565903))
      AS_COPY = True if getenv("AS_COPY", False) == "True" else False
      BOT_TOKEN = getenv("BOT_TOKEN", "6589617401:AAGi6DdOvoUKHom7CgO6ngsyI1-G9tAlxLQ")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002013698956").replace("\n", "-1002129248885").split(' '))
