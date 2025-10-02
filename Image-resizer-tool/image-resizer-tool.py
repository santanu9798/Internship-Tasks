import os
from PIL import Image

def resize_images(input_folder, output_folder, size=(300, 300), output_format="PNG"):
    """
    Resize and convert all images in a folder.

    :param input_folder: Path to folder containing images
    :param output_folder: Path to save resized images
    :param size: Tuple (width, height)
    :param output_format: Format to save images (e.g., 'PNG', 'JPEG')
    """

    # Create output folder if not exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        try:
            # Get file path
            file_path = os.path.join(input_folder, file_name)
            
            # Skip if it's not a file
            if not os.path.isfile(file_path):
                continue
            
            # Skip SVG files as they're vector graphics and don't resize well with PIL
            if file_name.lower().endswith('.svg'):
                print(f"Skipping SVG file: {file_name}")
                continue

            # Open image
            with Image.open(file_path) as img:
                # Resize
                resized_img = img.resize(size)

                # Convert extension
                base_name, _ = os.path.splitext(file_name)
                new_file = f"{base_name}.{output_format.lower()}"

                # Save image
                resized_img.save(os.path.join(output_folder, new_file), output_format)

                print(f"Saved {new_file}")

        except Exception as e:
            print(f"Could not process {file_name}: {e}")

# Example usage
if __name__ == "__main__":
    # Use absolute paths to avoid confusion
    script_dir = os.path.dirname(os.path.abspath(__file__))
    workspace_dir = os.path.dirname(script_dir)
    
    # Option 1: Use sample images from portfolio website
    input_folder = os.path.join(workspace_dir, "Build-portdolio-website", "static", "images")
    output_folder = os.path.join(script_dir, "resized_images")
    
    # Check if input folder exists
    if not os.path.exists(input_folder):
        print(f"Error: Input folder '{input_folder}' does not exist.")
        print("Please create an 'images' folder and add some image files to test the resizer.")
        exit(1)
    
    print(f"Input folder: {input_folder}")
    print(f"Output folder: {output_folder}")
    print("Starting image resize process...")
    
    resize_images(input_folder, output_folder, size=(400, 400), output_format="PNG")