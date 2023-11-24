#!/usr/bin/bash
pathFile="RussianHacker" 
pkg install python
cd ~/../usr/bin 
# команда
touch RussianHacker
echo "cd ~/$pathFile/ && python RussianHacker.py" >  RussianHacker
chmod +x RussianHacker
cd ~/
#конец
