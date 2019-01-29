"Test Return performance.esp"
	- I created this plugin to test and prove the problem documented here: https://cs.elderscrolls.com/index.php?title=Minimizing_your_Script#An_important_note_on_If_blocks_vs_early_Returns
	
	This Oblivion plugin contains a quest (XjTestReturnPerformanceQuest) that has a script (XjTestReturnPerformanceScript) which calls the function script "XjTestReturnPerformanceFunctionScript" 100 times per frame. "XjTestReturnPerformanceFunctionScript" contains around 3800 calls to the GetFPS and GetDistance functions. In total, the game runs through those functions 380000 times per frame. My testing procedure is documented in this forum post: https://forums.nexusmods.com/index.php?/topic/7325781-question-about-code-optimization/#entry67263966



I am releasing all of these files into the public domain. In places where this is not possible, I grant you a non-exclusive license to do whatever you want with your copy of these files.
