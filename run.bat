@echo off

echo "" > log.txt
set /a counter=0
:do
 echo %counter%
 python monitor.py>>log.txt
 set /a counter+=1
 timeout /t 10
:while
 if  %date% GEQ '27.02.2021' (goto next) else (goto do)
:next

echo next
pause&exit /b