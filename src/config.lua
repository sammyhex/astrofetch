-- General --
logo_color = '210-166-222' --RGB
text_color = '223-124-140'
-- separator_length = 28
plain_userhost = true

-- Zodiac stuff (comment if unwanted) --
season = require("user.zodiac_season")
custom_ascii = season.Logo

-- ENTRIES --
config_items = {
    'userhost',
    'separator',
    'date',
    'separator',
    'season',
    'symbol',
    'starts',
    'ends',
    'separator',
    'machine',
    'separator',
    'distro',
    'kernel',
    'separator',
    'uptime',
    'memory',
    'LAN',
}
