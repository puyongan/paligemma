from PIL import Image
import torch
from torchvision import transforms

transform = transforms.Compose([
    transforms.ToTensor()
])
img = Image.open('test_pic.png')
img = img.convert("RGB") 
img.save('test_pic.jpg')
print(img.mode)
img_tensor = transform(img)

print(img_tensor.shape)
