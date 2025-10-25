import eel  # type: ignore
import ollama  # type: ignore
import sys
import os

# Füge das Hauptverzeichnis zum Python-Pfad hinzu
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Jetzt kann llm_core importiert werden (falls es existiert)
try:
    from llm_core import main as llm_core
except ImportError:
    llm_core = None  # Falls nicht vorhanden, einfach ignorieren

model_name = "qwen2.5:14b"

# EEL GUI initialisieren
eel.init('web')

@eel.expose
def ask_jarvis(cmd):
    try:
        # Ollama Chat API korrekt verwenden
        resp = ollama.chat(
            model=model_name, 
            messages=[
                {"role": "user", "content": cmd}
            ]
        )
        
        # Response ist ein Dictionary mit 'message' key
        text = resp['message']['content']
        return text
        
    except ollama.ResponseError as e:
        return f"Ollama Fehler: {e.error}"
    except KeyError as e:
        return f"Unerwartetes Response-Format: {e}"
    except Exception as e:
        return f"Fehler: {str(e)}"

# GUI starten
if __name__ == "__main__":
    eel.start('index.html', size=(800, 600), block=True)