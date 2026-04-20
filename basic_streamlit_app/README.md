# Basic Streamlit App

This project builds an interactive Streamlit application to explore the Palmer's Penguins dataset. Users can filter and search penguin observations by a range of biological and categorical variables, with the full raw dataset available at the bottom of the app for reference.

**Disclaimer:** This is the first Streamlit app I built. I have since gained more Data Science and GitHub experience, so I will continue updating this project. Code can be found in main.py with instructions for running the app are in the comments at the top of that file.

## How to Run

1. Install Streamlit: pip install streamlit
2. Clone the repository and navigate to the project folder
3. Run the app: streamlit run main.py

## Dataset Overview

**Source:** [Palmer's Penguins (Excel)](https://tinyurl.com/PalmersPenguins)

The dataset contains observations of penguins across three species collected from islands in the Palmer Archipelago, Antarctica. Each row represents one penguin observation with the following variables:

- species — penguin species (Adelie, Chinstrap, Gentoo)
- island — island of observation
- bill_length_mm — bill length in millimeters
- bill_depth_mm — bill depth in millimeters
- flipper_length_mm — flipper length in millimeters
- body_mass_g — body mass in grams
- sex — sex of the penguin
- year — year of observation

## App Features

 Example of App's User Interface:

 
 <img width="1755" height="985" alt="image" src="https://github.com/user-attachments/assets/4e679d0f-f366-4c05-ad88-e05f8a318af0" />



The app allows users to:

- Filter penguin data interactively by any of the variables listed above
- Search and organize observations using left sidebar controls
- View the complete raw dataset in a table at the bottom of the app

## References

- Horst, A., Hill, A., & Gorman, K. (2020). *palmerpenguins: Palmer Archipelago (Antarctica) Penguin Data.* [https://tinyurl.com/PalmersPenguins](https://tinyurl.com/PalmersPenguins)
- Streamlit Documentation: [https://docs.streamlit.io](https://docs.streamlit.io)
