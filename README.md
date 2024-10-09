
# Pennyworth

**Pennyworth** is a Python-based file organization tool named after Alfred Pennyworth, the loyal and efficient butler of Bruce Wayne. Just like Alfred, this app ensures your files are well-organized and where they need to be, following customizable rules based on your preferences.

## Features

- **Custom Rules for Folder Organization:** 
  - Set different rules for any folder to match your workflow.
- **File Name-Based Rules:**
  - Sort files based on name patterns, such as:
    - Starts with a specific string
    - Ends with a specific extension
    - Contains certain keywords or phrases
- **Automation for Seamless Management:**
  - Automatically sorts and moves files to the appropriate folder without manual intervention.

## Requirements

- Python 3.x
- Required Libraries:
  - PySide6

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/remosrulloda/pennyworth.git
    ```

2. Navigate into the project directory:

    ```bash
    cd pennyworth
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the app:

    ```bash
    python pennyworth.py
    ```

2. Define your sorting rules:
   - You can specify rules for different folders based on file names, extensions, or the source of download.
   
3. Let **Pennyworth** take care of your files by automating the sorting and organization process.

## Example

If you download images from a specific website, **Pennyworth** can automatically move them to an "Images" folder. Similarly, it can move all `.pdf` files with "invoice" in the name to your "Invoices" folder.

## Future Enhancements

- More advanced rule customization
- Better GUI for easier rule creation and management

## Contributing

Feel free to open issues or submit pull requests if you'd like to contribute to the project!

## License

This project is licensed under the MIT License.
