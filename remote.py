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
switches.add_argument('-p', '--play', action="store_const", const="play", dest="action", default=None, help="Toggle play/pause")
switches.add_argument('-s', '--stop', action="store_const", const="stop", dest="action", default=None, help="Stop the playback")
switches.add_argument('-f', '--forward', action="store_const", const="forward", dest="action", default=None, help="Go to the next track")
switches.add_argument('-b', '--back', action="store_const", const="back", dest="action", default=None, help="Go the the previous track")
switches.add_argument('--pause', action="store_const", const="pause", dest="action", default=None, help="Pause the playback")
args = parser.parse_args()

class Connection:
  def __init__(self):
    self.player = dbus.SessionBus().get_object(amarokbus, playerpath)

  # The Pause method seems to be a toggle like play/pause.
  # This method will only pause
  def pause(self):
    status = self.player.GetStatus()
    # I believe that status[0].real being 1 is paused...?
    if status[0].real == 0:
      self.player.Pause()
    else:
      return


if __name__ == "__main__":
  that = Connection()
  commands = {
      'play':that.player.PlayPause,
      'stop':that.player.Stop,
      'back':that.player.Prev,
      'forward':that.player.Next,
      'pause':that.pause
      }
  commands[args.action]()

