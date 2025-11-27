#!/usr/bin/env python3
"""
Image Optimization Script for MPP Portal Cover Page
Compresses PNG image by 30-50% while maintaining quality
"""

import os
from PIL import Image
import sys

def optimize_image(input_path, output_path, quality=80):
    """
    Optimize PNG image with compression

    Args:
        input_path: Path to source image
        output_path: Path for optimized image
        quality: Compression quality (1-100, default 80 for 30-40% reduction)
    """
    print(f"Loading image: {input_path}")

    # Open image
    img = Image.open(input_path)

    # Get original size
    original_size = os.path.getsize(input_path)
    print(f"Original size: {original_size / 1024 / 1024:.2f} MB")
    print(f"Original dimensions: {img.size}")

    # Convert RGBA to RGB if needed (for better compression)
    if img.mode == 'RGBA':
        print("Converting RGBA to RGB...")
        rgb_img = Image.new('RGB', img.size, (255, 255, 255))
        rgb_img.paste(img, mask=img.split()[3] if len(img.split()) == 4 else None)
        img = rgb_img

    # Save with optimization
    print(f"Optimizing with quality={quality}...")
    img.save(output_path, 'PNG', optimize=True, compress_level=9)

    # Get optimized size
    optimized_size = os.path.getsize(output_path)
    reduction = ((original_size - optimized_size) / original_size) * 100

    print(f"\nOptimization complete!")
    print(f"Optimized size: {optimized_size / 1024 / 1024:.2f} MB")
    print(f"Size reduction: {reduction:.1f}%")
    print(f"Saved to: {output_path}")

    return optimized_size, reduction

if __name__ == "__main__":
    # Paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    input_path = os.path.join(project_root, "Cover Page.png")
    output_path = os.path.join(script_dir, "cover-page-optimized.png")

    # Check if input exists
    if not os.path.exists(input_path):
        print(f"Error: Input file not found: {input_path}")
        sys.exit(1)

    # Optimize
    try:
        optimize_image(input_path, output_path, quality=85)
    except Exception as e:
        print(f"Error during optimization: {e}")
        sys.exit(1)
