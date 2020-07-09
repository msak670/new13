# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name" : "Popup Alert Website",
    "author" : "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Website",
    "summary": """
    
     show simple popup on website, Work portfolio, Disclaimer Content, Any information.
    
                    """,
    "description": """
    
    This module useful to show simple popups, advertisement banner, New Product Information, Alert Message, Warning, Notifications, Work portfolio, Disclaimer Content, Any information on the website.
    
                    """,
    "version":"13.0.1",
    "depends" : ["base", "website", "portal"],
    "application" : True,
    "data" : [
        
              "views/popup.xml",
              "views/res_config_settings_view.xml",
              "views/website_view.xml"
            
            ],
    "images": ["static/description/background.png", ],
    "auto_install":False,
    "installable" : True,
    "price": 15,
    "currency": "EUR"   
}
