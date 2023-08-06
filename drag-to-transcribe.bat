@echo off
cls

if %1 == "" goto end
python fwtf.py "%~1"
pause

:end