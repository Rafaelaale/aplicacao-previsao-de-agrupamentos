import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from pathlib import Path
import nbformat
from nbclient import NotebookClient

p = Path("coletando_dados_sem_rotulo.ipynb")
with p.open("r", encoding="utf-8-sig") as f:
    nb = nbformat.read(f, as_version=4)

NotebookClient(nb, timeout=None, kernel_name="python311").execute()

with p.open("w", encoding="utf-8-sig", newline="") as f:
    nbformat.write(nb, f)

print("Notebook executado e saídas salvas.")
