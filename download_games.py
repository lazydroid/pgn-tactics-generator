#!/usr/bin/env python
# encoding: utf-8
#
# Downloading chess puzzles for lichess.org
#
import argparse
import chess
import chess.pgn
import logging
import os
import sys
import requests
import chess
import re
import time
import datetime

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--token", metavar="TOKEN",default="",
					help="secret token for the lichess api")
parser.add_argument("username", metavar="USERNAME",
					help="Username in lichess")
parser.add_argument("--quiet", dest="loglevel",
					default=logging.DEBUG, action="store_const", const=logging.INFO,
					help="substantially reduce the number of logged messages")
parser.add_argument("--max", metavar="MAX",default="60",
					help="max number of games")
settings = parser.parse_args()
logging.basicConfig(format="%(message)s", level=settings.loglevel, stream=sys.stdout)

logging.debug("Downloading games for: "+settings.username)

response = requests.get('https://lichess.org/api/games/user/'+settings.username+'?max='+settings.max+'&token=' + settings.token+'&perfType=blitz,rapid,classical&opening=true')
#pgn = str(response.text)

now = datetime.datetime.now()
suffix = now.strftime( '%Y-%m-%d' )
with open("%s_%s_games.pgn" % (settings.username, suffix), "w") as all_games :
	all_games.write(response.text.encode('utf-8'))

logging.debug("Finished.")
