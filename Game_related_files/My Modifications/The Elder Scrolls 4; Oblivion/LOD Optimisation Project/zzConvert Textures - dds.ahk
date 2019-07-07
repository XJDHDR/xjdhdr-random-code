Loop, Files, %A_ScriptDir%\aaS - RAEVWD textures\*, FR
{
	StringReplace, TargetTexture, A_LoopFileLongPath, %A_ScriptDir%\aaS - RAEVWD textures\, ,
	StringReplace, ConvertedTextureDir, A_LoopFileDir, aaS - RAEVWD, aD - Converted - dds,
	StringTrimRight, NewFileName, A_LoopFileName, 3
	NewFileName := NewFileName . "dds"
	
	IfExist, %A_ScriptDir%\1 - AWLS textures\%TargetTexture%
		SourceTexture := A_ScriptDir . "\1 - AWLS textures\" . TargetTexture
	Else IfExist, %A_ScriptDir%\2 - Unofficial Official Mods Patch\Textures\%TargetTexture%
		SourceTexture := A_ScriptDir . "\2 - Unofficial Official Mods Patch\Textures\" . TargetTexture
	Else IfExist, %A_ScriptDir%\3 - Unofficial Shivering Isles Patch\Textures\%TargetTexture%
		SourceTexture := A_ScriptDir . "\3 - Unofficial Shivering Isles Patch\Textures\" . TargetTexture
	Else IfExist, %A_ScriptDir%\4 - Unofficial Oblivion Patch\Textures\%TargetTexture%
		SourceTexture := A_ScriptDir . "\4 - Unofficial Oblivion Patch\Textures\" . TargetTexture
	Else IfExist, %A_ScriptDir%\5 - Original SI assets\Textures\%TargetTexture%
		SourceTexture := A_ScriptDir . "\5 - Original SI assets\Textures\" . TargetTexture
	Else IfExist, %A_ScriptDir%\6 - Original Oblivion assets\Textures\%TargetTexture%
		SourceTexture := A_ScriptDir . "\6 - Original Oblivion assets\Textures\" . TargetTexture
	Else IfExist, %A_ScriptDir%\7 - Frostcrag Spire assets\Textures\%TargetTexture%
		SourceTexture := A_ScriptDir . "\7 - Frostcrag Spire assets\Textures\" . TargetTexture
	Else
		SourceTexture := A_ScriptDir . "\6 - Original Oblivion assets\Textures\" . TargetTexture
	
	IfNotExist, %ConvertedTextureDir%\
		FileCreateDir, %ConvertedTextureDir%\

	IfInString, NewFileName, lod
	{
		RunWait, %ComSpec% /c ""%A_ScriptDir%\ImageMagick\magick.exe" convert "%SourceTexture%" "%ConvertedTextureDir%\%NewFileName%" 1>>"%A_ScriptDir%\out-dds.txt" 2>>"%A_ScriptDir%\errors-dds.txt"", , Min,
		Continue
	}

	IfInString, NewFileName, _g.
	{
		RunWait, %ComSpec% /c ""%A_ScriptDir%\ImageMagick\magick.exe" convert "%SourceTexture%" "%ConvertedTextureDir%\%NewFileName%" 1>>"%A_ScriptDir%\out-dds.txt" 2>>"%A_ScriptDir%\errors-dds.txt"", , Min,
		Continue
	}

	RunWait, %ComSpec% /c ""%A_ScriptDir%\ImageMagick\magick.exe" convert "%SourceTexture%" -colorspace RGB -filter point -resize 50`%`% -colorspace sRGB "%ConvertedTextureDir%\%NewFileName%" 1>>"%A_ScriptDir%\out-dds.txt" 2>>"%A_ScriptDir%\errors-dds.txt"", , Min,
}
