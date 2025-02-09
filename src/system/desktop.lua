local function trim_compositor(desktop)
    desktop = desktop:gsub("wayland", "")
                    :gsub("x11", "")
    return desktop
end

local function process_env_variable(env)
    env = env:sub(1, 1):upper() .. env:sub(2)
    return env
end

local function check_env_variable(env_variable)
    local desktop_environment
    if env_variable then
        desktop_environment = process_env_variable(env_variable)
    else
        desktop_environment = "Desktop Environment"
    end
    return desktop_environment
end

local function clarify(desktop)
    desktop = trim_compositor(desktop)
    return desktop
end

local desktop_env = check_env_variable(os.getenv("DESKTOP_SESSION"))

return clarify(desktop_env)
