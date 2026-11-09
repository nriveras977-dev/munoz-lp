import numpy as np
from PIL import Image

def process_logo(input_path: str, output_path: str):
    img = Image.open(input_path).convert("RGBA")
    arr = np.array(img, dtype=float)
    
    # Background color estimation (top corners are warm white ~ [245, 246, 240])
    bg_corners = np.mean([arr[5, 5, :3], arr[5, -5, :3], arr[-5, 5, :3], arr[-5, -5, :3]], axis=0)
    
    diff = np.sqrt(np.sum((arr[:, :, :3] - bg_corners)**2, axis=2))
    mask = diff > 20
    
    coords = np.argwhere(mask)
    y0, x0 = coords.min(axis=0)
    y1, x1 = coords.max(axis=0)
    
    # Calculate center and make it a clean square bounding box with small padding
    cy = (y0 + y1) // 2
    cx = (x0 + x1) // 2
    radius = max((y1 - y0) // 2, (x1 - x0) // 2) + 6
    
    crop_x0 = max(0, cx - radius)
    crop_y0 = max(0, cy - radius)
    crop_x1 = min(img.width, cx + radius)
    crop_y1 = min(img.height, cy + radius)
    
    cropped = img.crop((crop_x0, crop_y0, crop_x1, crop_y1))
    
    # Make background transparent where diff from corner color is very small
    cropped_arr = np.array(cropped)
    cropped_diff = np.sqrt(np.sum((cropped_arr[:, :, :3] - bg_corners)**2, axis=2))
    
    # Smooth alpha mask for edges
    alpha = np.clip((cropped_diff - 12) / 10.0, 0.0, 1.0) * 255.0
    cropped_arr[:, :, 3] = alpha.astype(np.uint8)
    
    result = Image.fromarray(cropped_arr)
    result.save(output_path, "PNG")
    print(f"Logo processed and saved to {output_path} (size: {result.size})")

if __name__ == "__main__":
    process_logo("c:/Users/Usuario/Downloads/muñoz lp/logo.jpg", "c:/Users/Usuario/Downloads/muñoz lp/logo.png")
