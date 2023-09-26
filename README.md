# HerikaMindMap
For use with the Herika AI Skyrim mod: https://www.nexusmods.com/skyrimspecialedition/mods/89931?tab=description

Requires the use of DwemerDistro (Herika Full).

Built on top of ChromaViz: https://github.com/mtybadger/chromaviz/tree/main

Will only work if you have generated at least 50 memories with Herika.
You will need to restart the application for new memories to appear. 

![alt text](https://i.imgur.com/l7CK5HF.png)
[alt text](https://i.imgur.com/6wUFRj4.png)

**To Build:**
pyinstaller HerikaMindMap.spec

**To Run:**
./dist/HerikaMindMap.exe

**Arguments:**
--ip
Address of ChromaDB (e.g. http://192.168.86.123:8000/)
