import os
import zipfile
import json
import shutil
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

def extract_costumes(sb3_file, output_dir):
    # Create the output folder if it doesn't exist (Assets parent folder)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with zipfile.ZipFile(sb3_file, 'r') as zip_ref:
        # Extract the contents of the .sb3 file 
        zip_ref.extractall('temp_sb3')  # Unzip the contents into a temporary directory

        # Path to the project.json file
        json_file_path = 'temp_sb3/project.json'

        # Open and read the project.json file
        with open(json_file_path, 'r') as f:
            project_data = json.load(f)

        # Look for all sprites and their costumes
        for sprite in project_data['targets']:
            # Skip the stage (it's usually the first target)
            if sprite.get('isStage', False):
                continue

            if 'costumes' in sprite:
                # Create a subfolder for each sprite inside the "Assets" folder
                sprite_folder = os.path.join(output_dir, sprite['name'])
                if not os.path.exists(sprite_folder):
                    os.makedirs(sprite_folder)

                for costume in sprite['costumes']:
                    if 'md5ext' in costume:
                        # Get the costume's file name (e.g., 'Melon33.png')
                        costume_name = costume['name'] + '.' + costume['dataFormat']
                        costume_file_path = 'temp_sb3/' + costume['md5ext']

                        # Check if the costume file exists and move it to the sprite's subfolder
                        if os.path.exists(costume_file_path):
                            shutil.copy(costume_file_path, os.path.join(sprite_folder, costume_name))
                        else:
                            print(f"Costume file {costume_name} not found.")
                    else:
                        print(f"No 'md5ext' field found for costume {costume['name']}.")

    # Clean up the temporary directory
    shutil.rmtree('temp_sb3')
    print(f"All costumes have been saved to {output_dir}.")

def create_spritesheet(input_folder, sprite_folder, output_file, sprite_width, sprite_height, images_per_row=5):
    # Get all images from the sprite folder
    images = []
    for file in os.listdir(sprite_folder):
        if file.endswith('.png'):
            image_path = os.path.join(sprite_folder, file)
            images.append(Image.open(image_path))

    # Calculate the size of the final spritesheet
    rows = (len(images) + images_per_row - 1) // images_per_row  # Round up to the next row
    sheet_width = images_per_row * sprite_width
    sheet_height = rows * sprite_height

    # Create a new blank image for the spritesheet
    spritesheet = Image.new('RGBA', (sheet_width, sheet_height))

    # Place the images in the spritesheet
    x_offset = 0
    y_offset = 0
    for index, image in enumerate(images):
        # Resize each image to the target size (if needed)
        image = image.resize((sprite_width, sprite_height))

        # Paste the image into the spritesheet
        spritesheet.paste(image, (x_offset, y_offset))

        # Update offsets
        x_offset += sprite_width
        if x_offset >= sheet_width:
            x_offset = 0
            y_offset += sprite_height

    # Save the spritesheet
    spritesheet.save(output_file)
    print(f"Spritesheet for {sprite_folder} saved as {output_file}")

def process_sprites(input_folder, sprite_width, sprite_height, images_per_row=5):
    # Process each subfolder (each sprite) in the input folder
    for sprite_folder in os.listdir(input_folder):
        sprite_folder_path = os.path.join(input_folder, sprite_folder)
        if os.path.isdir(sprite_folder_path):
            # Create output file name for each sprite's spritesheet
            output_file = os.path.join(input_folder, f'{sprite_folder}_spritesheet.png')

            # Create a spritesheet for the current sprite folder
            create_spritesheet(input_folder, sprite_folder_path, output_file, sprite_width, sprite_height, images_per_row)

def run():
    # Create the main window
    root = tk.Tk()
    root.title("Scratch Project to Spritesheets")

    # Function to handle the file selection
    def browse_file():
        file_path = filedialog.askopenfilename(filetypes=[("Scratch Project Files", "*.sb3")])
        if file_path:
            sb3_file_path.set(file_path)

    def create_sprites():
        sb3_file = sb3_file_path.get()
        if not sb3_file:
            messagebox.showerror("Error", "Please select a Scratch project file!")
            return

        # Create the "Assets" folder as the parent folder
        assets_folder = filedialog.askdirectory(title="Select Location for 'Assets' Folder")
        if not assets_folder:
            messagebox.showerror("Error", "Please select a location for the 'Assets' folder!")
            return
        
        # Add 'Assets' to the path
        output_folder = os.path.join(assets_folder, 'Assets')
        
        # Step 1: Extract costumes
        extract_costumes(sb3_file, output_folder)

        # Step 2: Create spritesheets
        sprite_width = 64  # Modify as needed
        sprite_height = 64  # Modify as needed
        process_sprites(output_folder, sprite_width, sprite_height)

        messagebox.showinfo("Success", "'Assets' folder with spritesheets created successfully!")

    # Variable to hold the file path
    sb3_file_path = tk.StringVar()

    # Create the UI elements
    tk.Label(root, text="Select a Scratch Project (.sb3)").pack(padx=10, pady=10)
    tk.Entry(root, textvariable=sb3_file_path, width=50).pack(padx=10, pady=5)
    tk.Button(root, text="Browse", command=browse_file).pack(padx=10, pady=5)
    tk.Button(root, text="Create Spritesheets", command=create_sprites).pack(padx=10, pady=20)

    # Start the GUI
    root.mainloop()

if __name__ == "__main__":
    run()
