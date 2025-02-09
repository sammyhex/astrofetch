local user = os.getenv("USER")

if user == nil then return "user" end

return user
