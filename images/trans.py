from PIL import Image
from pathlib import Path

input_path = Path(r"C:\Users\lenovo\Desktop\myblog\rizhaojinshan.jpg")
output_path = input_path.with_suffix(".webp")

img = Image.open(input_path).convert("RGB")
img.save(output_path, "WEBP", quality=80)

print("转换完成：", output_path)