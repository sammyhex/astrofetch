require("system.file_handling")

local function match_pretty_name(line)
    if line:match("^PRETTY_NAME") then
        line = line:gsub("^.*=", ""):sub(2, -2)
        return line
    else
        return 1
    end
end

local function match_contents(os_info_contents)
    local distro = "OO"
    for line in os_info_contents:gmatch("[^\r\n]+") do
        line = match_pretty_name(line)
        if not (line == 1) then return line end
    end
    return 1
end

local function find_distribution(file_contents)
    return match_contents(file_contents)
end

local distribution_file_location = "/etc/os-release"
local empty_file_warning = "Linux distribution"

local file_contents = read_file_contents(distribution_file_location)

if file_contents ~= 1 then return find_distribution(file_contents) else return empty_file_warning end
