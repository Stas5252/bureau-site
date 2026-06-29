import os
from PIL import Image, ImageDraw, ImageFont

def create_placeholders():
    folders = ['concept', 'decor', 'dresscode', 'production', 'lineup', 'cake']
    base_dir = "images"
    
    # Create beautiful aesthetic colors
    colors = {
        'concept': (200, 190, 180),
        'decor': (190, 180, 170),
        'dresscode': (50, 50, 150),
        'production': (150, 150, 150),
        'lineup': (40, 40, 120),
        'cake': (220, 210, 200)
    }
    
    os.makedirs(base_dir, exist_ok=True)
    
    for folder in folders:
        folder_path = os.path.join(base_dir, folder)
        os.makedirs(folder_path, exist_ok=True)
        color = colors.get(folder, (200, 200, 200))
        
        for i in range(1, 4):  # Generate 3 images per section
            img = Image.new('RGB', (800, 1000), color=color)
            d = ImageDraw.Draw(img)
            text = f"{folder.upper()} PHOTO {i}"
            
            # Since we might not have a reliable font, just draw some shapes or use default
            try:
                # Try to use a default or basic font
                font = ImageFont.truetype("arial.ttf", 40)
            except IOError:
                font = ImageFont.load_default()
                
            # We'll just draw a nice border and some text
            d.rectangle([(20, 20), (780, 980)], outline=(255,255,255), width=5)
            # Center text manually for load_default
            d.text((50, 450), text, fill=(255,255,255))
            
            img.save(os.path.join(folder_path, f"photo_{i}.jpg"))
            print(f"Generated {folder}/photo_{i}.jpg")

if __name__ == "__main__":
    create_placeholders()
