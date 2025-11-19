import os
from pathlib import Path

import pandas as pd

input_dir = Path("Datasets")

output_dir = Path("datasets_csv")
output_dir.mkdir(exist_ok=True)

for excel_path in input_dir.glob("*.xls*"):
    print(f"Converting {excel_path.name}...")

    df = pd.read_excel(excel_path)

    csv_name = excel_path.stem + ".csv"
    csv_path = output_dir / csv_name
    
    df.to_csv(csv_path, index=False)

print("Done converting all Excel files.")
