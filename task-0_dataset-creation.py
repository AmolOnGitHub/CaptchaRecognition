from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os
import random
import time

from others.general import WORD_LIST


IMAGE_SIZE = (250, 100)
FONT_FOLDER = "fonts"
DATA_FOLDER = "dataset"

CAPITALIZATIONS = 2
CAPITALIZATION_PROB = 0.4
NOISE_LEVELS = 2
NOISE_INCREMENT = 10

font_files = os.listdir(FONT_FOLDER)
text_colors = ["black", "red", "green", "blue", "purple", "orange", "pink", "brown"]


def random_capitalization(word):
    return ''.join(char.upper() if random.random() < CAPITALIZATION_PROB else char.lower() for char in word)


### Creates an image given a word, font path, background color, text color and font size
def create_base_image(word, font_path, bg_color="white", text_color="black", font_size=30):

    img = Image.new("RGB", IMAGE_SIZE, color=bg_color)
    draw = ImageDraw.Draw(img)

    # Try loading font
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        print(f"Cannot load font {font_path}, using default")
        font = ImageFont.load_default()
    

    # Calculate text size and center it

    text_width = draw.textlength(word, font)
    text_height = font_size
    text_x = (IMAGE_SIZE[0] - text_width) // 2
    text_y = (IMAGE_SIZE[1] - text_height) // 2

    draw.text((text_x, text_y), word, font=font, fill=text_color)

    return img


### Adds gaussian noise to an image
def add_noise(image, noise_level):
    arr = np.array(image)
    noise = np.random.normal(0, noise_level, arr.shape)
    noisy_arr = np.clip(arr + noise, 0, 255)

    return Image.fromarray(noisy_arr.astype(np.uint8))


if __name__ == "__main__":

    # Create/clear folders
    if os.path.exists(DATA_FOLDER):
        for folder in os.listdir(DATA_FOLDER):
            folder_path = os.path.join(DATA_FOLDER, folder)
            if os.path.isdir(folder_path):
                for file in os.listdir(folder_path):
                    file_path = os.path.join(folder_path, file)
                    os.remove(file_path)
                os.rmdir(folder_path)


    os.makedirs(f"{DATA_FOLDER}/easy", exist_ok=True)
    os.makedirs(f"{DATA_FOLDER}/hard", exist_ok=True)
    os.makedirs(f"{DATA_FOLDER}/bonus", exist_ok=True)


    total_permutations = (len(WORD_LIST) * len(font_files) * CAPITALIZATIONS * (NOISE_LEVELS + 1) * 3 + len(WORD_LIST)) * 2
    count = 1

    print(f"Total permutations: {total_permutations}")
    time.sleep(1)


    ## Easy set

    font_path = os.path.join(FONT_FOLDER, 'Arial.ttf')
    for word in WORD_LIST:
        img = create_base_image(word.title(), font_path, font_size=30)

        img.save(f'{DATA_FOLDER}/easy/{word}_small.png')
        print(f"Created {DATA_FOLDER}/easy/{word}_small.png | {count}/{total_permutations} | {count/total_permutations*100:.2f}%")

        img = create_base_image(word.title(), font_path, font_size=40)

        img.save(f'{DATA_FOLDER}/easy/{word}_large.png')
        print(f"Created {DATA_FOLDER}/easy/{word}_large.png | {count}/{total_permutations} | {count/total_permutations*100:.2f}%")
        count += 1


    ## Hard set

    for word in WORD_LIST:
        random_capitalizations = set()
        while len(random_capitalizations) < CAPITALIZATIONS:
            t = random_capitalization(word)
            random_capitalizations.add(t)
        
        uid = 0
        
        for capitalized_word in random_capitalizations:
            text_color = random.choice(text_colors)

            for font_file in font_files:
                font_name = font_file.split(".")[0]
                font_path = os.path.join(FONT_FOLDER, font_file)

                img_small = create_base_image(capitalized_word, font_path, text_color=text_color, font_size=30)
                img_large = create_base_image(capitalized_word, font_path, text_color=text_color, font_size=40)

                img_small.save(f'{DATA_FOLDER}/hard/{word}_{uid}_{font_name}_{00}_small.png')
                print(f"Created {DATA_FOLDER}/hard/{word}_{uid}_{font_name}_{00}_small.png | {count}/{total_permutations} | {count/total_permutations*100:.2f}%")
                count += 1

                img_large.save(f'{DATA_FOLDER}/hard/{word}_{uid}_{font_name}_{00}_large.png')
                print(f"Created {DATA_FOLDER}/hard/{word}_{uid}_{font_name}_{00}_large.png | {count}/{total_permutations} | {count/total_permutations*100:.2f}%")
                count += 1

                for noise in range(NOISE_INCREMENT, NOISE_INCREMENT * NOISE_LEVELS + 1, NOISE_INCREMENT):
                    noisy_img_small = add_noise(img_small, noise)
                    noisy_img_large = add_noise(img_large, noise)

                    noisy_img_small.save(f'{DATA_FOLDER}/hard/{word}_{uid}_{font_name}_{noise}_small.png')
                    print(f"Created {DATA_FOLDER}/hard/{word}_{uid}_{font_name}_{noise}_small.png | {count}/{total_permutations} | {count/total_permutations*100:.2f}%")
                    count += 1

                    noisy_img_large.save(f'{DATA_FOLDER}/hard/{word}_{uid}_{font_name}_{noise}_large.png')
                    print(f"Created {DATA_FOLDER}/hard/{word}_{uid}_{font_name}_{noise}_large.png | {count}/{total_permutations} | {count/total_permutations*100:.2f}%")
                    count += 1


            uid += 1                


    ## Bonus set

    text_colors.remove("green")
    text_colors.remove("red")

    for word in WORD_LIST:
        random_capitalizations = set()
        while len(random_capitalizations) < CAPITALIZATIONS:
            t = random_capitalization(word)
            random_capitalizations.add(t)
        
        uid = 0
        
        for capitalized_word in random_capitalizations:
            text_color = random.choice(text_colors)

            for background_color in ["green", "red"]:
                if background_color == "red":
                    capitalized_word[::-1]

                for font_file in font_files:
                    font_name = font_file.split(".")[0]
                    font_path = os.path.join(FONT_FOLDER, font_file)

                    img_small = create_base_image(capitalized_word, font_path, text_color=text_color, bg_color=background_color, font_size=30)
                    img_large = create_base_image(capitalized_word, font_path, text_color=text_color, bg_color=background_color, font_size=40)

                    img_small.save(f'{DATA_FOLDER}/bonus/{word}_{uid}_{font_name}_{00}_small_{background_color}.png')
                    print(f"Created {DATA_FOLDER}/bonus/{word}_{uid}_{font_name}_{00}_small_{background_color}.png | {count}/{total_permutations} | {count/total_permutations*100:.2f}%")
                    count += 1

                    img_large.save(f'{DATA_FOLDER}/bonus/{word}_{uid}_{font_name}_{00}_large_{background_color}.png')
                    print(f"Created {DATA_FOLDER}/bonus/{word}_{uid}_{font_name}_{00}_large_{background_color}.png | {count}/{total_permutations} | {count/total_permutations*100:.2f}%")
                    count += 1

                    for noise in range(NOISE_INCREMENT, NOISE_INCREMENT * NOISE_LEVELS + 1, NOISE_INCREMENT):
                        noisy_img_small = add_noise(img_small, noise)
                        noisy_img_large = add_noise(img_large, noise)

                        noisy_img_small.save(f'{DATA_FOLDER}/bonus/{word}_{uid}_{font_name}_{noise}_small_{background_color}.png')
                        print(f"Created {DATA_FOLDER}/bonus/{word}_{uid}_{font_name}_{noise}_small_{background_color}.png | {count}/{total_permutations} | {count/total_permutations*100:.2f}%")
                        count += 1

                        noisy_img_large.save(f'{DATA_FOLDER}/bonus/{word}_{uid}_{font_name}_{noise}_large_{background_color}.png')
                        print(f"Created {DATA_FOLDER}/bonus/{word}_{uid}_{font_name}_{noise}_large_{background_color}.png | {count}/{total_permutations} | {count/total_permutations*100:.2f}%")
                        count += 1

                uid += 1                
