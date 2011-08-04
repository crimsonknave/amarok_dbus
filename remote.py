#!/usr/bin/env python2

#  
#  Copyright (C) 2011 Joseph Henrich
# 
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
# 
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
# 
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


import dbus
import argparse

amarokbus = "org.kde.amarok"
playerpath = "/Player"

parser = argparse.ArgumentParser(description="Provides a dbus interface to control amarok.  Mostly for Docky")
switches = parser.add_mutually_exclusive_group(required=True)
switches.add_argument('-p', '--play', '--pause', action="store_const", const="play", dest="action", default=None, help="Toggle play/pause")
switches.add_argument('-s', '--stop', action="store_const", const="stop", dest="action", default=None, help="Stop the playback")
switches.add_argument('-f', '--forward', action="store_const", const="forward", dest="action", default=None, help="Go to the next track")
switches.add_argument('-b', '--back', action="store_const", const="back", dest="action", default=None, help="Go the the previous track")
args = parser.parse_args()

if __name__ == "__main__":
  player = dbus.SessionBus().get_object(amarokbus, playerpath)
  commands = {
      'play':player.PlayPause,
      'stop':player.Stop,
      'back':player.Prev,
      'forward':player.Next
      }
  commands[args.action]()

