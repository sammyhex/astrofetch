require("system.file_handling")

local function attempt_vendor_read(hardware_info)
    if hardware_info == 1 then hardware_info = "Unknown hardware/platform" end
    return hardware_info
end

local function attempt_board_read(hardware_info)
    if hardware_info == 1 then return '' end
    return hardware_info:gsub("%(.-%)", "")
end

local product_family_location = "/sys/devices/virtual/dmi/id/product_family"
local board_name_location = "/sys/devices/virtual/dmi/id/board_name"
local system_vendor_location = "/sys/devices/virtual/dmi/id/sys_vendor"
local unknown_product_family = "To be filled by O.E.M.\n"

local hardware_name = read_file_contents(product_family_location)

if (hardware_name == unknown_product_family) or (hardware_name == 1) then
    hardware_name = read_file_contents(board_name_location)
    hardware_name = attempt_board_read(hardware_name)
end

if hardware_name == '' then
    hardware_name = read_file_contents(system_vendor_location)
    hardware_name = attempt_vendor_read(hardware_name)
end

hardware_name = hardware_name:gsub("\n", "")
return hardware_name
