function Initialize()

	sFileToRead = SELF:GetOption('FileToRead')
	
end

function Update()

	hReadingFile = io.open(sFileToRead)
	if not hReadingFile then
		print('LuaReadFile: unable to open file at ' .. sFileToRead)
		return
	end
	
	-- READ FILE CONTENTS AND CLOSE.
	Contents = {}
	for Line in hReadingFile:lines() do
		table.insert(Contents, Line)
	end
	
	io.close(hReadingFile)
	return Contents
end

function getContents(index)
	if table.getn(Contents) >= index then
		if index == 1 then
			return Contents[index]
		else
			str = "    "
			str = str .. Contents[index]
			return str
		end
	else
		return ""
	end
end