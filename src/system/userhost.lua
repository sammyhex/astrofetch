local username = require("system.user")
local hostname = require("system.host")
return username .. "@".. hostname
