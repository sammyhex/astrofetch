require("system.file_handling")

local function add_commas(readable_uptime)
    return readable_uptime:gsub("([%a])%s", "%1, "):sub(1, -3)
end

local function translate_seconds(uptime_seconds, divisor)
    return math.floor(uptime_seconds / divisor)
end

local function get_remainder(uptime_seconds, modulus)
    return math.floor(uptime_seconds % modulus)
end

local function format_unit(uptime)
    --Removes 's' from unit word if an uptime of 1 is passed
    if uptime:sub(1, 2) == "1 " then
        uptime = uptime:sub(1, -3) .. " "
    end
    return uptime
end

local function check_seconds_inclusion(uptime)
    if uptime_seconds == false then
        uptime = uptime:gsub("..second.", "")
    end
    return uptime
end

local function calculate_readable_uptime(uptime_in_seconds)
    local readable_uptime, uptime_prefix, uptime_suffix, remainder_uptime
    if uptime_in_seconds < 60 then -- < 1 min
        uptime_prefix = format_unit(math.floor(uptime_in_seconds) .. " seconds ")
        uptime_suffix = ""
    elseif uptime_in_seconds < 3600 then -- < 1 hr
        uptime_prefix = format_unit(translate_seconds(uptime_in_seconds, 60) .. " minutes ")
        uptime_suffix = calculate_readable_uptime(get_remainder(uptime_in_seconds, 60))
      elseif uptime_in_seconds < 86400 then -- < 1 day
        uptime_prefix = format_unit(translate_seconds(uptime_in_seconds, 3600) .. " hours ")
        uptime_suffix = calculate_readable_uptime(get_remainder(uptime_in_seconds, 3600))
    elseif uptime_in_seconds < 604800 then -- < 1 week
        uptime_prefix = format_unit(translate_seconds(uptime_in_seconds, 86400) .. " days ")
        uptime_suffix = calculate_readable_uptime(get_remainder(uptime_in_seconds, 86400))
    elseif uptime_in_seconds < 31556952 then -- < 1 year
        uptime_prefix = format_unit(translate_seconds(uptime_in_seconds, 604800) .. " weeks ")
        uptime_suffix = calculate_readable_uptime(get_remainder(uptime_in_seconds, 604800))
    else -- > 1 year
        uptime_prefix = format_unit(translate_seconds(uptime_in_seconds, 31556952) .. " years ")
        uptime_suffix = calculate_readable_uptime(get_remainder(uptime_in_seconds, 31556952))
    end
    return uptime_prefix .. uptime_suffix
end

local uptime_file_location = "/proc/uptime"
local empty_uptime = " -- "
local uptime = read_file_contents(uptime_file_location)

if  uptime ~= 1 then
    uptime = uptime:gsub("%s.*$", "")
    uptime = tonumber(uptime)
    return add_commas(calculate_readable_uptime(uptime))
else
    return empty_uptime
end
