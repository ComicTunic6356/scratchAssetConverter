# Scratch Project to Spritesheets

This program allows you to extract costumes from a Scratch project (.sb3) and create spritesheets for each sprite. The extracted assets and the generated spritesheets are saved in a newly created "Assets" folder. The program is packaged as an executable, so you don’t need to have Python installed to use it.

## Features

- Extracts costumes from a Scratch project (.sb3).
- Creates spritesheets for each sprite.
- Allows you to select the location for the output folder.
- Excludes the stage from being processed.
- Easy-to-use graphical interface.

## Files

- `main.py`: The main Python script responsible for extracting assets and creating spritesheets.
- `scratchAssetConverter.exe`: The compiled executable version of the script. This version can be run on Windows without needing Python.
- `assets`: The folder where the spritesheets and extracted assets are saved.
- `README.md`: This file.

## Requirements

If you are running the Python version of the program:

- **Python 3.13.2+**: Make sure the correct version of Python is installed.
- **Required libraries**:

  - `zipfile`
  - `json`
  - `shutil`
  - `Pillow` (Python Imaging Library)
  - `tkinter` (for the GUI)

  You can install the required libraries by running:
  pip install pillow
  in the terminal

**How to use the .exe**:
  Run the executable by double-clicking on it.
  Select a Scratch project file (.sb3): Use the "Browse" button to select the .sb3 project you want to extract costumes from.
  Select the location for the "Assets" folder: Choose where you want the "Assets" folder to be created. This folder will contain the sprite folders and spritesheets.
  Create spritesheets: After selecting the location, click "Create Spritesheets." The program will extract costumes, create the spritesheets, and save them in the specified folder.
  The "Assets" folder will contain:

      Folders for each sprite in the Scratch project.
      A spritesheet for each sprite containing its costumes.

**How to use the source code file**:
  Install the required libraries:

First, make sure you have Python installed. Then install the required libraries:

pip install pillow

Run the script:

    python main.py

    Follow the same steps as for the executable version to select your .sb3 file and output folder.

Troubleshooting

    Missing files or folders: If the program can't find the Scratch project file, make sure the path is correct and that the .sb3 file exists.
    Spritesheet not created: Check that there are actually costumes for the sprite in the Scratch project. If no costumes are available, no spritesheet will be created.
    Permission errors: If you encounter permission issues, make sure the folder you’re saving to is accessible and that you have write permissions.

    License

This project is licensed under the MIT License - see the LICENSE file for details.
Contributions

Feel free to fork this repository and submit pull requests with improvements or bug fixes!