#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import uno
import unohelper
from pythonscript import ScriptContext
import os.path

def connect_script_context(host='localhost', port='2002', namedpipe=None):
    UNO_RESOLVER = "com.sun.star.bridge.UnoUrlResolver"
    UNO_DESKTOP = "com.sun.star.frame.Desktop"
    localCtx = uno.getComponentContext()
    localSmgr = localCtx.ServiceManager
    resolver = localSmgr.createInstanceWithContext(UNO_RESOLVER, localCtx)
    if namedpipe is None:
        uno_string = 'uno:socket,host=%s,port=%s;urp;StarOffice.ComponentContext' % (host, port)
    else:
        uno_string = 'uno:pipe,name=%s;urp;StarOffice.ComponentContext' % namedpipe
    ctx = resolver.resolve(uno_string)
    smgr = ctx.ServiceManager
    XSCRIPTCONTEXT = ScriptContext(ctx,
                                   smgr.createInstanceWithContext(UNO_DESKTOP, ctx),
                                   None)
    return XSCRIPTCONTEXT

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test.ods')
url  = unohelper.systemPathToFileUrl(file)
XSCRIPTCONTEXT = connect_script_context(namedpipe='librepipe')
desktop = XSCRIPTCONTEXT.getDesktop()
doc = desktop.loadComponentFromURL(url, "_blank", 0, ())
sheet = doc.getSheets().getByIndex(0)
sheet.getCellByPosition(0,0).Value = 999
doc.store()

