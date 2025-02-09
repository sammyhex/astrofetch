require("system.file_handling")

local function concatenate_values(total, used)
    local memory_as_string
    if used == 0.0 then 
        memory_as_string = total .. "GB"
    else
        memory_as_string = total .. "GB (" .. used .. "G used)"
    end
    return memory_as_string
end

local function make_table_readable(memory_table)
    memory_table["memory"] = concatenate_values(memory_table["memory"], memory_table["mem_used"])
    memory_table["mem_used"] = nil
    memory_table["swap"] = concatenate_values(memory_table["swap"], memory_table["swap_used"])
    memory_table["swap_used"] = nil
    return memory_table
end

local function convert_to_gb(memory_in_kb, round_to_whole)
    local memory_in_gb
    if round_to_whole == true then
        memory_in_gb = memory_in_kb / 1000000
        memory_in_gb = math.floor(memory_in_gb)
    else
        memory_in_gb = memory_in_kb / 100000
        memory_in_gb = math.floor(memory_in_gb) / 10
    end
    return memory_in_gb
end

local function format_memory_table(memory_table)
    local memory_used = memory_table["memory"] - memory_table["mem_available"]
    local swap_used = memory_table["swap"] - memory_table["swap_available"]

    memory_table["mem_available"] = nil
    memory_table["swap_available"] = nil

    memory_table["memory"] = convert_to_gb(memory_table["memory"], true)
    memory_table["swap"] = convert_to_gb(memory_table["swap"], true)
    memory_table["mem_used"] = convert_to_gb(memory_used, false)
    memory_table["swap_used"] = convert_to_gb(swap_used, false)

    memory_table = make_table_readable(memory_table)
    return memory_table
end

local function format_memory_to_number(line)
    line = line:gsub("%s", ""):gsub("^.*:", ""):sub(1, -3)
    return line
end

local function process_memory_file(memory_info)
    local memory_table = {memory=0, mem_available=0, mem_used=0, swap=0, swap_available=0, swap_used=0}
    local count = 0
    for line in memory_info:gmatch("[^\r\n]+") do
        if line:match("^MemTotal") then
            memory_table["memory"] = format_memory_to_number(line)
            count = count + 1
        elseif line:match("^MemAvailable") then
            memory_table["mem_available"] = format_memory_to_number(line)
            count = count + 1
        elseif line:match("^SwapTotal") then
            memory_table["swap"] = format_memory_to_number(line)
            count = count + 1
        elseif line:match("^SwapFree") then
            memory_table["swap_available"] = format_memory_to_number(line)
            count = count + 1
        end
    end

    if count == 4 then
        memory_table = format_memory_table(memory_table)
    else
        return 1
    end
    return memory_table
end

local memory_file_location = "/proc/meminfo"
local empty_memory_warning = "Memory not found"
local memory_info = read_file_contents(memory_file_location)

if not (memory_info == 1) then
    local memory_values = process_memory_file(memory_info)
    return memory_values["memory"]
else
    return empty_memory_warning
end
