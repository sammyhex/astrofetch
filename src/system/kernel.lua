require("system.file_handling")

local function find_kernel_version(kernel_info_line)
    local kernel_version = kernel_info_line:gsub("%s+", ""):gsub("%-.*", "")
    return kernel_version
end

local kernel_file_location = "/proc/sys/kernel/osrelease"
local empty_file_warning = "Unknown kernel"

local file_contents = read_file_contents(kernel_file_location)

if file_contents ~= 1 then return find_kernel_version(file_contents) else return empty_file_warning end
