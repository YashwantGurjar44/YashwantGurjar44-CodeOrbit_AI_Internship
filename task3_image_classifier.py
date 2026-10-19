import torch
from torchvision import models, transforms
from PIL import Image
import urllib.request
import os

def load_labels():
    labels_file = "imagenet_classes.txt"
    if not os.path.exists(labels_file):
        url = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
        urllib.request.urlretrieve(url, labels_file)
    with open(labels_file, "r") as f:
        return [line.strip() for line in f.readlines()]

def classify_image(image_path):
    print("Loading MobileNetV2 model...")
    # Load pretrained model and set to evaluation mode
    weights = models.MobileNet_V2_Weights.DEFAULT
    model = models.mobilenet_v2(weights=weights)
    model.eval()

    # Preprocessing pipeline required for MobileNetV2
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    try:
        img = Image.open(image_path).convert('RGB')
    except Exception as e:
        print(f"Error loading image: {e}")
        return

    # Apply transforms and add a batch dimension
    img_tensor = preprocess(img).unsqueeze(0)
    
    print("Running inference...")
    with torch.no_grad():
        output = model(img_tensor)
        
    # Convert logits to probabilities
    probabilities = torch.nn.functional.softmax(output[0], dim=0)
    top5_prob, top5_catid = torch.topk(probabilities, 5)
    
    categories = load_labels()
    print("\n--- Predictions ---")
    for i in range(top5_prob.size(0)):
        score = top5_prob[i].item() * 100
        label = categories[top5_catid[i].item()]
        print(f"{label}: {score:.2f}%")

if __name__ == "__main__":
    target_image = "sample_image.jpg"
    if os.path.exists(target_image):
        classify_image(target_image)
    else:
        print(f"Please place an image named '{target_image}' in the same folder to run.")