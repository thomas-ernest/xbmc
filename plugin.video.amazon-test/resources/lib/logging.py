#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xbmc
from resources.lib.common import Globals, Settings


def Log(msg, level=xbmc.LOGNOTICE):
    if not hasattr(Log, 's'):
        Log.s = Settings()
    if not hasattr(Log, 'p'):
        Log.p = Globals().addon.getAddonInfo('name')
    if level == xbmc.LOGDEBUG and Log.s.verbLog:
        level = xbmc.LOGNOTICE
    msg = '[%s] %s' % (Log.p, msg)
    xbmc.log(msg.encode('utf-8'), level)
Log.ERROR = xbmc.LOGERROR