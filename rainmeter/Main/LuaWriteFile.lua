function Initialize()
	sFileToWrite = SELF:GetOption('FileToWrite')
end -- function Initialize

function Update()

	hWritingFile = io.open(sFileToWrite)
	if not hWritingFile then
		print('LuaWriteFile: unable to open file at ' .. sFileToWrite)
		return
	end
	sContents = SELF:GetOption('Contents')

    return sContents
end -- function Update

function writeToFile(Contents)

    file = io.open("C:\\Users\\total\\OneDrive\\Documents\\Rainmeter\\Skins\\TestSkin\\Main\\input.txt", "a")
	file:write(Contents, "\n")
    file:close()
end