import requests
import os
from PIL import Image
from bs4 import BeautifulSoup
import base64
from io import BytesIO

# Define folders for storing compressed and original images
compressed_folder = "compressed_images"
original_folder = "original_images"
os.makedirs(compressed_folder, exist_ok=True)
os.makedirs(original_folder, exist_ok=True)

# URL of the pages to fetch images from
links = [
    "https://www.clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-blog-section-creator",
    "https://www.clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-blog-ideas-generator",
    "https://www.clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-blog-title-generator",
    "https://www.clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-blog-intro-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-blog-conclusion-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-blog-tags-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-blog-summary-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-confirmation-email-creator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-discount-email-creator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-testimonial-email-creator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-promotional-email-creator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-follow-up-email-creator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-twitter-post-creator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-discount-promotion-creator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-social-media-bio-creator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-facebook-ads-creator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-instagram-captions-creator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-ai-social-media-post-creator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-event-promotion-creator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-google-ads-headlines-creator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-google-ads-description-creator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-youtube-video-title-creator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-youtube-video-description-creator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-youtube-video-tagkeywords-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-website-faq-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-website-faq-answers-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-website-review-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-website-title-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-website-meta-tags-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-website-meta-description-creator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-website-about-us-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-website-terms-and-conditions-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-website-privacy-policy-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-vision-of-the-company-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-mission-of-the-company-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-academic-essay-writer",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-article-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-paragraph-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-content-rewriter",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-product-description-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-product-name-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-product-summarize-text",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-grammar-checker",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-creative-story-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-startup-name-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-pros--cons-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-job-description-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-rejection-letter-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-offer-letter-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-promotion-letter-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-motivational-quote-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-song-lyrics-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-short-story-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-wedding-quote-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-birthday-wish-quote-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-story-outline-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-story-title--subtitle-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-story-ideas-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-tiktok-video-script-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-tiktok-video-caption-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-tiktok-video-ideas-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-instagram-story-ideas-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-instagram-post-ideas-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-instagram-reel-ideas-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-career-success-story-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-business-success-story-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-startup-success-story-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-matrimonial-website-success-story-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-blog-post-seo-meta-description-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-home-page-seo-meta-description-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-product-page-seo-meta-description-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-eid-ul-fitr-letter-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-eid-ul-fitr-storybook-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-eid-party-planning-checklist-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-image-prompt-ideas-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-instagram-hashtag-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-tiktok-video-keywords-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-product-review-generator",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-image-prompt-optimizer",
    "https://clevercreator.ai/resources/blog/ai-content-creator/how-to-use-the-ai-facebook-post-creator"
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


# Function to convert base64 string to an image
def base64_to_image(base64_string):
    image_data = base64.b64decode(base64_string)
    image = Image.open(BytesIO(image_data))
    return image

# Function to create a subfolder
def create_sub_folder(parent_folder, folder_name):
    folder_path = os.path.join(parent_folder, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    return folder_path

# Function to fetch the HTML content of a page
def fetch_page(link, headers):
    try:
        response = requests.get(link, headers=headers)
        if response.status_code == 200:
            print("Page fetched successfully")
            return response.text
        else:
            print("Failed to fetch page")
            return None
    except requests.RequestException as e:
        print("Failed to fetch page")
        return None

# Function to parse the HTML content and extract the title and images
def parse_page(html):
    soup = BeautifulSoup(html, "html.parser")
    title = soup.find("h1").text.split("AI")[1].strip()
    images = soup.find_all("img")
    return title, images

# Function to save the original image
def save_original_image(image, image_name, folder, type="png"):
    image.save(f"{folder}/{image_name}.{type}", type)
    return f"{folder}/{image_name}.{type}"

# Function to save the compressed image
def save_compressed_image(image, image_name, folder, type="webp", quality=70):
    image.save(f"{folder}/{image_name}.{type}", type, quality=quality)
    return f"{folder}/{image_name}.{type}"



# Function to compare the sizes of the original and compressed images
def compare_images(original_image_path, compressed_image_path):
    original_size = os.path.getsize(original_image_path)
    compressed_size = os.path.getsize(compressed_image_path)
    print(f"Original size: {original_size} bytes")
    print(f"Compressed size: {compressed_size} bytes")
    print(f"Reduction: {((original_size - compressed_size) / original_size) * 100:.2f}%")

# Function to download and save images from a list of image sources
def download_and_save_images(title, images):
    count = 0
    # Create subfolder for compressed images
    compressed_images = create_sub_folder(compressed_folder, title)
    # make a txt file to store the alt text
    alt_text_file = None
    if os.path.exists(f"{compressed_images}/alt_text.txt"):
        alt_text_file = open(f"{compressed_images}/alt_text.txt", "w")
    else:
        alt_text_file = open(f"{compressed_images}/alt_text.txt", "a")
    # Create a subfolder for storing original images
    original_images = create_sub_folder(original_folder, title)
    for image in images:

        # Check if the image source is a base64 encoded image
        if "data:image" in image["src"]:
            count += 1
            print(f"\nDownloading image {count}\n")
            image_link = image["src"]
            image_name = "image_" + str(count)
            image_data = image_link.split(",")[1]

            alt_text = image.get("alt", f"{title}_image_{count}")
            alt_text_file.write(f"{image_name}: {alt_text}\n")
            print(f"Alt text: {alt_text}")

            
            # Decode the base64 image
            image = base64_to_image(image_data)

            # Save the original image
            original_image_path = save_original_image(image, image_name, original_images, "png")
            
            # Compress and save the image
            compressed_image_path = save_compressed_image(image, image_name, compressed_images, "webp", 70)
            
            # Compare the original and compressed images
            compare_images(original_image_path, compressed_image_path)

#loop through the links and download images
for link in links:
    # Fetch the HTML content of the page
    html = fetch_page(link, headers)
    if html:
        # Parse the HTML content to extract the title and images
        title, images = parse_page(html)
        print(f"Title: {title}")
        # Download and save the images
        download_and_save_images(title, images)
    else:
        print("Failed to download images")
