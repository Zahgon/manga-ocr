import sys
import time
from pathlib import Path

import fire
import numpy as np
import pyperclip
from PIL import Image
from PIL import UnidentifiedImageError
from loguru import logger

from manga_ocr import MangaOcr


def are_images_identical(img1, img2):
    pass


def process_and_write_results(mocr, img_or_path, write_to):
    pass


def get_path_key(path):
    pass


def run(
    read_from="clipboard",
    write_to="clipboard",
    pretrained_model_name_or_path="kha-white/manga-ocr-base",
    force_cpu=False,
    delay_secs=0.1,
    verbose=False,
):
    """
    Run OCR in the background, waiting for new images to appear either in system clipboard, or a directory.
    Recognized texts can be either saved to system clipboard, or appended to a text file.

    :param read_from: Specifies where to read input images from. Can be either "clipboard", or a path to a directory.
    :param write_to: Specifies where to save recognized texts to. Can be either "clipboard", or a path to a text file.
    :param pretrained_model_name_or_path: Path to a trained model, either local or from Transformers' model hub.
    :param force_cpu: If True, OCR will use CPU even if GPU is available.
    :param verbose: If True, unhides all warnings.
    :param delay_secs: How often to check for new images, in seconds.
    """
    pass


if __name__ == "__main__":
    fire.Fire(run)
