require("system.file_handling")

local function find_hostname_from_file(file_contents, empty_file_warning)
    local hostname = file_contents:gsub("%s+", "")
    if hostname == "" then
        return empty_file_warning
    else
        return hostname
    end
end

local function try_file(hostname_file_location, empty_file_warning)
    local file_contents = read_file_contents(hostname_file_location)
    if not (file_contents == 1) then
        return find_hostname_from_file(file_contents, empty_file_warning)
    else
        return empty_file_warning
    end
end

local env_host = os.getenv("HOSTNAME")
local hostname_file_location = "/etc/hostname"
local empty_file_warning = "localhost"

if env_host == nil then
    return try_file(hostname_file_location, empty_file_warning)
else
    return env_host
end
