"""Run the notebook's setup and training cells without a Jupyter kernel."""
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT / 'notebooks')
notebook = json.loads(Path('HDS-CDT2025-Exercise-3-Segmentation-ImplementUNet.ipynb').read_text())
namespace = {'__name__': '__main__'}
# Skip plotting and final evaluation cells; retain notebook training behavior.
for index in (1, 3, 5, 6, 8, 9, 14, 17, 19, 20):
    source = ''.join(notebook['cells'][index]['source'])
    if index == 17:
        source += '\nassert torch.cuda.is_available(), "GPU unavailable; refusing unintended CPU training"\n'
    print(f'Executing notebook cell {index}', flush=True)
    exec(compile(source, f'notebook-cell-{index}', 'exec'), namespace)
print('Training finished at the 500-epoch target.', flush=True)
