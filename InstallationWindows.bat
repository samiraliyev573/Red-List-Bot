@IF errorlevel 1 exit /b 1
call conda create -y -n projenv python=3.8
call conda activate projenv
call conda install -y pytorch torchvision torchaudio cpuonly -c pytorch
call conda install -y nltk
pip3 install pygame
pip3 install playsound
pip3 install gtts
pip3 install numpy
cd %USERPROFILE%\Documents\GitHub\Red-List-Bot\src
python gui.py