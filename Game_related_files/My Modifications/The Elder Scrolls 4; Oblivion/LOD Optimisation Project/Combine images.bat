Set /P rows="How many images per row?"

"%~dp0ImageMagick\magick.exe" montage %* -geometry 1x1^<+0+0 -tile %rows%x -background transparent -gravity NorthWest "%~dp0Combination.png"

Pause
