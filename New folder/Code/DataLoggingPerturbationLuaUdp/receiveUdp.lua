package.cpath = package.cpath .. ";core.dll"
local socket = require("socket.core")
host = host or "192.168.0.2"
port = port or 8888
-- if arg then
    -- host = arg[1] or host
    -- port = arg[2] or port
-- end
print("Binding to host '" ..host.. "' and port " ..port.. "...")
udp = assert(socket.udp())
assert(udp:setsockname(host, port))
assert(udp:settimeout(5))
ip, port = udp:getsockname()
assert(ip, port)
print("Waiting packets on " .. ip .. ":" .. port .. "...")
while 1 do
	dgram, ip, port = udp:receivefrom()
	if dgram == '17' then
		print("Echoing '" .. dgram .. "' to " .. ip .. ":" .. port)
		break
    end
end
