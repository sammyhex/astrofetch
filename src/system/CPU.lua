require("system.file_handling")

local function get_cpu_model(model_name)
    model_name = model_name:gsub("^.*:", ""):sub(2)
    model_name = model_name:gsub("Processor", "")
    if model_name:match("with") then model_name = model_name:gsub("with.*", "") end
    return model_name
end

local function find_cpu_model(cpu_file_contents)
    local cpu_model
    for line in cpu_file_contents:gmatch("[^\r\n]+") do
        if line:match("^model name") then return get_cpu_model(line) end
    end
end

local cpu_info_file_location = "/proc/cpuinfo"
local empty_file_warning = "Unknown CPU"

local cpu_file_contents = read_file_contents(cpu_info_file_location)

if cpu_file_contents ~= 1 then return find_cpu_model(cpu_file_contents) else return empty_file_warning end
