from PIL import Image, ImageFilter
import os

def enhance_assets():
    assets_dir = "assets"
    if not os.path.exists(assets_dir):
        print("No assets folder")
        return
        
    for filename in os.listdir(assets_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            path = os.path.join(assets_dir, filename)
            try:
                with Image.open(path) as img:
                    # Convert to RGBA if needed to preserve transparency during operations
                    original_mode = img.mode
                    
                    # 1. Upscale by 2x using Lanczos (high quality resampling)
                    new_size = (int(img.width * 2), int(img.height * 2))
                    img_resized = img.resize(new_size, Image.Resampling.LANCZOS)
                    
                    # 2. Apply Unsharp Mask to improve crispness
                    img_sharpened = img_resized.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
                    
                    # Save back
                    img_sharpened.save(path, quality=95)
                    print(f"Enhanced {filename} (from {img.width}x{img.height} to {new_size[0]}x{new_size[1]})")
            except Exception as e:
                print(f"Error enhancing {filename}: {e}")

if __name__ == "__main__":
    enhance_assets()
