Loop, Files, %A_ScriptDir%\aaS - RAEVWD Meshes\*, D
{
	SubDirectory := A_LoopFileName
	Loop, Files, %A_ScriptDir%\aaS - RAEVWD Meshes\%SubDirectory%\*, FR
	{
		StringReplace, TargetMesh, A_LoopFileLongPath, %A_ScriptDir%\aaS - RAEVWD Meshes\%SubDirectory%\Meshes\, ,
		StringReplace, ConvertedMeshDir, A_LoopFileDir, aaS - RAEVWD Meshes, aD - Converted - nif,
		StringTrimRight, AlternateFileName, TargetMesh, 8
		AlternateFileName := AlternateFileName . ".nif"
		
		IfNotExist, %ConvertedMeshDir%\
			FileCreateDir, %ConvertedMeshDir%\

		IfExist, %A_ScriptDir%\2 - Unofficial Official Mods Patch\Meshes\%TargetMesh%
		{
			FileCopy, %A_ScriptDir%\2 - Unofficial Official Mods Patch\Meshes\%TargetMesh%, %ConvertedMeshDir%\%A_LoopFileName%, Flag
		}
		Else IfExist, %A_ScriptDir%\3 - Unofficial Shivering Isles Patch\Meshes\%TargetMesh%
		{
			FileCopy, %A_ScriptDir%\3 - Unofficial Shivering Isles Patch\Meshes\%TargetMesh%, %ConvertedMeshDir%\%A_LoopFileName%, Flag
		}
		Else IfExist, %A_ScriptDir%\4 - Unofficial Oblivion Patch\Meshes\%TargetMesh%
		{
			FileCopy, %A_ScriptDir%\4 - Unofficial Oblivion Patch\Meshes\%TargetMesh%, %ConvertedMeshDir%\%A_LoopFileName%, Flag
		}
		Else IfExist, %A_ScriptDir%\5 - Original SI assets\Meshes\%TargetMesh%
		{
			FileCopy, %A_ScriptDir%\5 - Original SI assets\Meshes\%TargetMesh%, %ConvertedMeshDir%\%A_LoopFileName%, Flag
		}
		Else IfExist, %A_ScriptDir%\6 - Original Oblivion assets\Meshes\%TargetMesh%
		{
			FileCopy, %A_ScriptDir%\6 - Original Oblivion assets\Meshes\%TargetMesh%, %ConvertedMeshDir%\%A_LoopFileName%, Flag
		}
		Else IfExist, %A_ScriptDir%\7 - Frostcrag Spire assets\Meshes\%TargetMesh%
		{
			FileCopy, %A_ScriptDir%\7 - Frostcrag Spire assets\Meshes\%TargetMesh%, %ConvertedMeshDir%\%A_LoopFileName%, Flag
		}
		Else IfExist, %A_ScriptDir%\2 - Unofficial Official Mods Patch\Meshes\%AlternateFileName%
		{
			FileCopy, %A_ScriptDir%\2 - Unofficial Official Mods Patch\Meshes\%AlternateFileName%, %ConvertedMeshDir%\%A_LoopFileName%, Flag
		}
		Else IfExist, %A_ScriptDir%\3 - Unofficial Shivering Isles Patch\Meshes\%AlternateFileName%
		{
			FileCopy, %A_ScriptDir%\3 - Unofficial Shivering Isles Patch\Meshes\%AlternateFileName%, %ConvertedMeshDir%\%A_LoopFileName%, Flag
		}
		Else IfExist, %A_ScriptDir%\4 - Unofficial Oblivion Patch\Meshes\%AlternateFileName%
		{
			FileCopy, %A_ScriptDir%\4 - Unofficial Oblivion Patch\Meshes\%AlternateFileName%, %ConvertedMeshDir%\%A_LoopFileName%, Flag
		}
		Else IfExist, %A_ScriptDir%\5 - Original SI assets\Meshes\%AlternateFileName%
		{
			FileCopy, %A_ScriptDir%\5 - Original SI assets\Meshes\%AlternateFileName%, %ConvertedMeshDir%\%A_LoopFileName%, Flag
		}
		Else IfExist, %A_ScriptDir%\6 - Original Oblivion assets\Meshes\%AlternateFileName%
		{
			FileCopy, %A_ScriptDir%\6 - Original Oblivion assets\Meshes\%AlternateFileName%, %ConvertedMeshDir%\%A_LoopFileName%, Flag
		}
		Else IfExist, %A_ScriptDir%\7 - Frostcrag Spire assets\Meshes\%AlternateFileName%
		{
			FileCopy, %A_ScriptDir%\7 - Frostcrag Spire assets\Meshes\%AlternateFileName%, %ConvertedMeshDir%\%A_LoopFileName%, Flag
		}
		Else
			FileAppend, Not Found:`n%TargetMesh%`n%AlternateFileName%`n`n, %A_ScriptDir%\Log.txt,
	}
}
