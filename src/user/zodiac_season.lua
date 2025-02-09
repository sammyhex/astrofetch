require("user.astrology.aquarius")
require("user.astrology.cancer")
require("user.astrology.gemini")
require("user.astrology.libra")
require("user.astrology.pisces")
require("user.astrology.scorpio")
require("user.astrology.virgo")
require("user.astrology.aries")
require("user.astrology.capricorn")
require("user.astrology.leo")
require("user.astrology.sagittarius")
require("user.astrology.taurus")

local function prev_i(i)
    if (i - 1 == 0) then return 12 end
    return i - 1 
end

local function affirm_season(current, previous)
    if os.date("%d") < current.Start_Day then
        return previous
    else
        return current
    end
end

local function current_season_id(zodiac_signs, i)
    if zodiac_signs[i].Start_Mon == os.date("%m") then
        local current_zodiac = zodiac_signs[i]
        local previous_zodiac = zodiac_signs[prev_i(i)]
        return affirm_season(current_zodiac, previous_zodiac)
    end
end

local zodiac_signs = {Aquarius, Pisces, Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius, Capricorn} -- These must be in order by month

local i
for i = 1, 12 do
     local current_sign = current_season_id(zodiac_signs, i)
     if (current_sign ~= True) then return current_sign end
end
