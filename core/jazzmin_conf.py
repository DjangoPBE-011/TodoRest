# ---------------------------------------------------------------------------
# Jazzmin (admin panel theme)
# https://django-jazzmin.readthedocs.io/
# ---------------------------------------------------------------------------

JAZZMIN_SETTINGS = {
    # sarlavhalar
    "site_title": "Todo Admin",
    "site_header": "Todo",
    "site_brand": "Todo Admin",
    # "site_logo": "images/logo.png",
    "welcome_sign": "Admin panelga xush kelibsiz",
    "copyright": "Todo Project",

    # yuqoridagi qidiruv maydoni qaysi model bo'yicha qidiradi
    "search_model": ["accounts.CustomUser"],
    "user_avatar": "avatar",  # foydalanuvchi avatari (CustomUser'da rasm maydoni bo'lsa, nomini yozing)
    "custom_css": "css/custom.css",
    
    
    # yuqori menyu
    "topmenu_links": [
        {"name": "Bosh sahifa", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Saytni ochish", "url": "/", "new_window": True},
    ],

    # chap menyu
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": ["token_blacklist"],
    "hide_models": [],
    "order_with_respect_to": ["accounts", "todo", "base", "auth"],

    # ikonlar (Font Awesome 5)
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.Group": "fas fa-users",
        "accounts.CustomUser": "fas fa-user",
        
        "todo": "fas fa-clipboard-list",     # sidebar'dagi "Todo" bo'limi
        "todo.Category": "fas fa-tags",      # Categories
        "todo.Task": "fas fa-tasks",         # Tasks
    },
    
    "default_icon_parents": "fas fa-folder",
    "default_icon_children": "fas fa-circle",

    # model tahrirlash sahifasi ko'rinishi
    "changeform_format": "horizontal_tabs",

    # admin panelda temani jonli tanlash oynasi (tanlab bo'lgach False qiling)
    "show_ui_builder": True,
}

