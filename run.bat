@echo off
chcp 65001 >nul

cd /d "%~dp0"

echo run[1/2]

start "llama-server" /min cmd /c "cd llama-b11429-bin-win-cuda-12.4-x64 && llama-server.exe -m ..\Qwen2.5-Coder-7B-Instruct-heretic.gguf -c 4096 -ngl 99 --port 8080"

echo run ai url...(1~5)
timeout /t 8 /nobreak >nul

echo [2/2] run TXT-RAG
python TXT-RAG.py

pause