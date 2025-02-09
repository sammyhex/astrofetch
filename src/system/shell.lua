local function find_shell_version()
    local version = "_version_goes_here"
    return version
end

local function get_shell(environment_variable)
    local shell
    if environment_variable == nil then
        shell = "Linux Shell"
    else
        shell = environment_variable:gsub("bin", ""):gsub("usr", ""):gsub("/", "")
    end
    return shell
end

local environment_shell = os.getenv("SHELL")
local shell = get_shell(environment_shell)
return shell
