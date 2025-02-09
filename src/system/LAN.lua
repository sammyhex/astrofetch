require("system.file_handling")

local function check_connectivity(local_ip, network_err)
    if local_ip == nil then
        local_ip = network_err
    end
    return local_ip
end

local function check_for_local_ip(line)
    if not line:match("127.0.0.") then
        return line:gsub("/32 host LOCAL", ""):gsub("%s", ""):gsub("|--", "")
    end
end

local function get_ip_from_contents(network_file_contents)
    local local_ip
    for line in network_file_contents:gmatch("[^|]+") do
        if line:match("32 host LOCAL") then
            local_ip = check_for_local_ip(line)
            if local_ip then return local_ip end
        end
    end
end

local network_info_file_location = "/proc/net/fib_trie"
local network_info = read_file_contents(network_info_file_location)
local network_err = "No connection"

if network_info ~= 1 then return check_connectivity(get_ip_from_contents(network_info, network_err)) else return network_err end
