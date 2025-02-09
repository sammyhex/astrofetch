function read_file_contents(file_location)
    local file_contents
    local data_file = io.open(file_location, "r")

    if data_file then
        file_contents = data_file:read("*all")
        data_file:close()
        return file_contents
    else
        return 1
    end
end
