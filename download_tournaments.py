#!/usr/bin/env python

"""Downloading chess puzzles for lichess.org"""

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

# tournaments
tournament_ids = [
'25MtoToy',
'E14kHVwX',
'tdntXNhy',
'sj5GoEdS',
'C4zdQLax',
'wobqi6QP',
'T4RW1ux2',
'nzw7OKBq']

#tournament_ids = [ 'YZbypMx0' ]
#tournament_ids = [ 'dec20bta' ]	# titled blitz arena 2020
tournament_ids = [ 'dec20lta' ]	# titled arena dec 2020

pgn = ""
for id in tournament_ids:
    print ('https://lichess.org/api/tournament/'+id+'/games')
    response = requests.get('https://lichess.org/api/tournament/'+id+'/games')
    pgn = pgn +'\n'+ response.text.encode('utf-8')

now = datetime.datetime.now()
suffix = now.strftime( '%Y-%m-%d' )
with open("%s_%s_games.pgn" % (tournament_ids[0], suffix), "w") as all_games :
	all_games.write(pgn)

logging.debug("Finished.")

