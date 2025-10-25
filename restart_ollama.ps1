Write-Host "🔍 Checking if Ollama is already running..."
$process = Get-Process | Where-Object { $_.ProcessName -eq "ollama" }
if ($process) {
    Write-Host "🛑 Ollama läuft bereits. Beende Prozess..."
    Stop-Process -Name "ollama" -Force
    Start-Sleep -Seconds 2
}
Write-Host "🚀 Starte Ollama neu..."
Start-Process "ollama" "serve"
Write-Host "✅ Ollama wurde neu gestartet!"
