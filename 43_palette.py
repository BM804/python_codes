"""Distinct Python example #43."""
from collections import Counter
try:
 from PIL import Image
 image=Image.open(input("Image path: ")).convert("RGB"); image.thumbnail((200,200)); print(Counter(image.getdata()).most_common(6))
except ImportError:print("Install Pillow: python -m pip install pillow")
