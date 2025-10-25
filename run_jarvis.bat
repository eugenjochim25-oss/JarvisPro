@echo off
echo ==============================
echo   🚀 Jarvis Pro Local Start
echo ==============================

:: Venv aktivieren
call venv\Scripts\Activate.bat

:: Fehlende Pakete installieren (nur beim ersten Start)
pip install --upgrade pip
pip install pyttsx3 SpeechRecognition pyaudio eel openwakeword sounddevice numpy

:: Ollama stoppen (falls schon laufend)
taskkill /IM ollama.exe /F >nul 2>&1

:: Ollama neu starten
start powershell -NoExit -Command "ollama serve"
timeout /t 5 >nul

:: KI-Core starten
start powershell -NoExit -Command "python llm_core\main.py"

:: System Bridge starten
start powershell -NoExit -Command "python system_bridge\bridge.py"

:: GUI + Wakeword starten
start powershell -NoExit -Command "python speech_ui\interface.py"
start powershell -NoExit -Command "python speech_ui\wakeword.py"

echo ==============================
echo Jarvis Pro sollte jetzt laufen!
echo ==============================
pause
