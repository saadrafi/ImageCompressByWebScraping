# Image Downloader and Compressor

This Python script allows you to download images from a specified webpage, save them in their original format, and then compress them to reduce their file size. The script uses the `requests` library to fetch the webpage content, `BeautifulSoup` to parse the HTML and extract image URLs, and the `Pillow` library to handle image compression.

## Features

- **Fetch Images from a Webpage**: The script can fetch all images from a specified webpage.
- **Save Original Images**: The original images are saved in a designated folder.
- **Compress Images**: The images are compressed and saved in a separate folder.
- **Compare Image Sizes**: The script compares the sizes of the original and compressed images to show the reduction in file size.
- **Base64 Image Handling**: Decodes and processes images embedded as base64 strings.

### Libraries Used
- `requests`: For fetching webpage content.
- `Pillow`: For image manipulation and compression.
- `BeautifulSoup` (from `bs4`): For parsing HTML content.
- `base64`: For decoding base64 image data.
- `os`: For creating and managing folders.
- `io.BytesIO`: For in-memory handling of binary image data.

## Requirements
### Prerequisites
1. Python 3.x installed on your system.

To run this script, you need to have Python installed on your computer. The project includes a virtual environment (`venv`) with all the required dependencies pre-installed. If you prefer to install the dependencies manually, you can use the `requirements.txt` file.

## How to Use

1. **Clone the Repository**: First, clone this repository to your local machine.

    ```bash
    git clone https://github.com/your-repository/image-downloader-compressor.git
    cd image-downloader-compressor
    ```

2. **Set Up the Virtual Environment**:
   - If you want to use the provided virtual environment, activate it:
     - On **Windows**:
       ```bash
       .\venv\Scripts\activate
       ```
     - On **macOS/Linux**:
       ```bash
       source venv/bin/activate
       ```
   - If you prefer to install the dependencies manually, skip this step and proceed to the next one.

3. **Install Dependencies (Optional)**: If you are not using the virtual environment, install the required Python packages using pip.

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Script**: Execute the script using Python.

    ```bash
    python script.py
    ```

5. **View the Results**: The script will create two folders:
    - `original_images`: Contains the original images downloaded from the webpage.
    - `compressed_images`: Contains the compressed versions of the images.

6. **Compare Image Sizes**: The script will print out the sizes of the original and compressed images, along with the percentage reduction in file size.

## Customization

- **Change the Webpage URL**: You can change the URL of the webpage from which images are fetched by modifying the `link` variable in the script.
  
    ```python
    link = "https://example.com"
    ```

- **Adjust Compression Quality**: You can adjust the quality of the compressed images by modifying the `quality` parameter in the `save_compressed_image` function.

    ```python
    save_compressed_image(image, image_name, folder, "webp", quality=70)
    ```

- **Change Image Format**: You can change the format of the compressed images by modifying the `type` parameter in the `save_compressed_image` function.

    ```python
    save_compressed_image(image, image_name, folder, "jpeg", quality=70)
    ```

## Running on Different Computers

To run this script on a different computer, follow these steps:

1. **Install Python**: Ensure that Python is installed on the computer. You can download it from [python.org](https://www.python.org/).

2. **Clone the Repository**: Clone the repository to the new computer.

    ```bash
    git clone https://github.com/your-repository/image-downloader-compressor.git
    cd image-downloader-compressor
    ```

3. **Set Up the Virtual Environment**:
   - If you want to use the provided virtual environment, activate it:
     - On **Windows**:
       ```bash
       .\venv\Scripts\activate
       ```
     - On **macOS/Linux**:
       ```bash
       source venv/bin/activate
       ```
   - If you prefer to install the dependencies manually, skip this step and proceed to the next one.

4. **Install Dependencies (Optional)**: If you are not using the virtual environment, install the required Python packages using pip.

    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Script**: Execute the script using Python.

    ```bash
    python script.py
    ```

## Example Output

```bash
Page fetched successfully
Title: How to Use the AI Facebook Post Creator

Downloading image 1

Original size: 123456 bytes
Compressed size: 65432 bytes
Reduction: 47.00%
```

---

## Notes
- If the webpage does not contain images or the images are not accessible, the script will output a message indicating the failure to download images.
- Ensure the provided URL is valid and accessible from the computer running the script.
- The compression quality can be adjusted in the `save_compressed_image` function by modifying the `quality` parameter.

---
---

### Notes on Virtual Environments

- The virtual environment (`venv`) included in this project is pre-configured with all the necessary dependencies. Activating it ensures that the script runs in an isolated environment with the correct versions of the libraries.
- If you prefer not to use the virtual environment, you can install the dependencies globally using `pip install -r requirements.txt`.
- If you create a new virtual environment, make sure to install the dependencies using `pip install -r requirements.txt`.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. We welcome any contributions, whether they are bug fixes, new features, or improvements to the documentation.

## Support

If you encounter any issues or have any questions, please open an issue on the GitHub repository.

---

Enjoy using the Image Downloader and Compressor! If you find it useful, consider giving it a star on GitHub.

