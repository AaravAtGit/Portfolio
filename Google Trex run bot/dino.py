import cv2
import numpy as np
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Load the T-Rex game site
driver = webdriver.Chrome()
driver.get("https://elgoog.im/t-rex/")

# Start the game
driver.find_element(By.TAG_NAME,"body").send_keys(Keys.SPACE)

# Continuously check for obstacles and jump if necessary
while True:
    # Take a screenshot of the game
    driver.save_screenshot("screenshot.png")

    # Load the screenshot using OpenCV
    screenshot = cv2.imread("screenshot.png")

    # Get the RGB value of a specific region of interest (ROI)
    roi = screenshot[300:340, 300:360]

    # Define the tolerance range
    tolerance = 20

    # Check if the ROI color is within the tolerance range of (83, 83, 83)
    if np.all(np.abs(roi - [83, 83, 83]) <= tolerance):
        # Jump to avoid the obstacle
        driver.find_element(By.TAG_NAME,"body").send_keys(Keys.SPACE)
        print("AHHHHH")

    # Delay to avoid overloading the CPU
    time.sleep(0.1)
