#!/usr/bin/env python3
"""
Embed Assets Script - Converts image and audio to Base64
and injects them into the HTML file
"""

import os
import base64

def file_to_base64(file_path):
    """Convert file to Base64 string"""
    with open(file_path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

def embed_assets():
    """Embed optimized image and audio into HTML"""

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    # File paths
    image_path = os.path.join(script_dir, "cover-page-optimized.png")
    audio_path = os.path.join(script_dir, "mpp-portal-voiceover.mp3")
    html_template_path = os.path.join(project_root, "src", "mpp-portal-scroll.html")
    html_output_path = os.path.join(project_root, "mpp-portal-scroll-complete.html")

    print("MPP Portal Asset Embedding")
    print("=" * 60)

    # Check files exist
    if not os.path.exists(image_path):
        print(f"Error: Image not found: {image_path}")
        return False

    if not os.path.exists(audio_path):
        print(f"Error: Audio not found: {audio_path}")
        return False

    if not os.path.exists(html_template_path):
        print(f"Error: HTML template not found: {html_template_path}")
        return False

    # Convert to Base64
    print("\nConverting image to Base64...")
    image_size = os.path.getsize(image_path)
    print(f"  Image size: {image_size / 1024 / 1024:.2f} MB")
    image_base64 = file_to_base64(image_path)
    print(f"  Base64 size: {len(image_base64) / 1024 / 1024:.2f} MB")

    print("\nConverting audio to Base64...")
    audio_size = os.path.getsize(audio_path)
    print(f"  Audio size: {audio_size / 1024:.2f} KB")
    audio_base64 = file_to_base64(audio_path)
    print(f"  Base64 size: {len(audio_base64) / 1024:.2f} KB")

    # Read HTML template
    print("\nReading HTML template...")
    with open(html_template_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Replace placeholders
    print("Embedding assets into HTML...")
    html_content = html_content.replace('PLACEHOLDER_IMAGE_BASE64', image_base64)
    html_content = html_content.replace('PLACEHOLDER_AUDIO_BASE64', audio_base64)

    # Write output HTML
    print(f"\nWriting complete HTML file...")
    with open(html_output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    output_size = os.path.getsize(html_output_path)
    print(f"  Output file: {html_output_path}")
    print(f"  Total size: {output_size / 1024 / 1024:.2f} MB")

    print("\n" + "=" * 60)
    print("SUCCESS! Complete HTML file ready for Articulate Rise")
    print("=" * 60)
    print(f"\nFile location: {html_output_path}")
    print("\nNext steps:")
    print("1. Open Articulate Rise")
    print("2. Add Block > Embed > Code")
    print("3. Copy and paste the entire HTML content")
    print("4. Set block height: 750px")
    print("5. Preview and test!")

    return True

if __name__ == "__main__":
    success = embed_assets()
    exit(0 if success else 1)
