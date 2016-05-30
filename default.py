# -*- coding: utf-8 -*-
#------------------------------------------------------------
# (c) 2016 - PAHO (Fruits-Entertainment.tv & Techcluster.net)
# Based on code from youtube addon
#------------------------------------------------------------
import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.alphacentauri'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')
fanart = 'special://home/addons/plugin.video.alphacentauri/fanart.jpg'

YOUTUBE_CHANNEL_ID = "ScienceAstronomy"

# Entry point
def run():
    plugintools.log("alphacentauri.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("alphacentauri.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="Alpha Centauri (1998)",
        url="plugin://plugin.video.youtube/playlist/PLBRf3zSvyQfQcKQpVOdr0JUry9BbX94u9/",
        thumbnail=icon,
        fanart=fanart,
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Alpha Centauri (1999)",
        url="plugin://plugin.video.youtube/playlist/PLBRf3zSvyQfSl_i1eiWSSd3ji069wY9zx/",
        thumbnail=icon,
        fanart=fanart,
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Alpha Centauri (2000)",
        url="plugin://plugin.video.youtube/playlist/PLBRf3zSvyQfRQKIKUU4ujZ8tA_staIxv0/",
        thumbnail=icon,
        fanart=fanart,
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Alpha Centauri (2001)",
        url="plugin://plugin.video.youtube/playlist/PLBRf3zSvyQfRcAzCPBE4fqiVB1EwcX0B0/",
        thumbnail=icon,
        fanart=fanart,
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Alpha Centauri (2002)",
        url="plugin://plugin.video.youtube/playlist/PLBRf3zSvyQfTE9aiRRnO2jLtq2BmgOECY/",
        thumbnail=icon,
        fanart=fanart,
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Alpha Centauri (2003)",
        url="plugin://plugin.video.youtube/playlist/PLBRf3zSvyQfR3x-JDs2DxjDCTiy-_spd6/",
        thumbnail=icon,
        fanart=fanart,
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Alpha Centauri (2004)",
        url="plugin://plugin.video.youtube/playlist/PLBRf3zSvyQfSQkXc-x0Xb7SHMfIPOQzgm/",
        thumbnail=icon,
        fanart=fanart,
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Alpha Centauri (2005)",
        url="plugin://plugin.video.youtube/playlist/PLBRf3zSvyQfTnkdtzpVUZeYQ9EZHcJh7o/",
        thumbnail=icon,
        fanart=fanart,
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Alpha Centauri (2006)",
        url="plugin://plugin.video.youtube/playlist/PLBRf3zSvyQfQ11gb_6j7Dm164iRNx5U7J/",
        thumbnail=icon,
        fanart=fanart,
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Alpha Centauri (alle Folgen 1-100)",
        url="plugin://plugin.video.youtube/playlist/PLBRf3zSvyQfSm285DCrQ-WFY3ewWQpmru/",
        thumbnail=icon,
        fanart=fanart,
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Alpha Centauri (alle Folgen 101-217)",
        url="plugin://plugin.video.youtube/playlist/PLBRf3zSvyQfSmqnz9rG9CjWso4to9WRUv/",
        thumbnail=icon,
        fanart=fanart,
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Alle Videos mit Prof. Harald Lesch",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID+"/",
        thumbnail=icon,
        fanart=fanart,
        folder=True )

run()