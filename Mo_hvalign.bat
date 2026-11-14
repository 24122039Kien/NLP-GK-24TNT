@echo off
rem Nhap dup de mo giao dien hvalign (can Python 3.10+ va: pip install -r requirements.txt)
chcp 65001 >nul
cd /d "%~dp0"
python -m hvalign app
if errorlevel 1 pause
