# MMAI891 - Natural Language Processing

## Cloning the Repository and Installing Dependencies

1. **Install Anaconda:**

   - **Windows:**
     1. Download the Anaconda installer from the [official Anaconda website](https://www.anaconda.com/products/distribution#download-section).
     2. Run the installer and follow the instructions.

   - **macOS:**
     1. Download the Anaconda installer for macOS from the [official Anaconda website](https://www.anaconda.com/products/distribution#download-section).
     2. Open the downloaded .pkg file and follow the installation instructions.

   - **Linux:**
     1. Download the Anaconda installer for Linux from the [official Anaconda website](https://www.anaconda.com/products/distribution#download-section).
     2. Open Terminal and navigate to the directory where the installer was downloaded.
     3. Run the installer using the command:
        ```
        bash Anaconda3-<version>-Linux-x86_64.sh
        ```
     4. Follow the instructions in the Terminal.

2. **Install Visual Studio Code (VS Code):**

   - Download and install Visual Studio Code from the [official VS Code website](https://code.visualstudio.com/).

3. **Install Git (Windows Users Only):**

   - Download and install Git from the [official Git website](https://git-scm.com/download/win).
   - Follow the installation instructions.

4. **Configure Git and Authenticate:**

   - After installing Git, open Git Bash or Command Prompt and configure your Git username and email. These details will be associated with your commits:
     ```
     git config --global user.name "Your Name"
     git config --global user.email "your.email@example.com"
     ```
   - To authenticate to GitHub, you can use a personal access token. Follow these steps:
     1. Generate a personal access token on GitHub by following the instructions [here](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token).
     2. Use the token to authenticate when prompted during a Git operation like `git clone` or `git push`.

5. **Setup Conda Environment and Jupyter Kernel:**

   - Open Terminal or Anaconda Prompt and create a new conda environment named `mmai891` with the following command:
     ```
     conda create --name mmai891 python=3.11
     ```
   - Activate the conda environment:
     ```
     conda activate mmai891
     ```
   - Install Jupyter Notebook in the conda environment:
     ```
     conda install jupyter
     ```
   - Create a Jupyter kernel with the same name as the conda environment:
     ```
     python -m ipykernel install --user --name mmai891 --display-name "mmai891"
     ```

6. **Clone the Repository:**

   - Use the following command to clone the repository to your local machine:
     ```
     git clone https://github.com/moezali1/MMAI891.git
     ```
   - This command downloads the repository and its contents into a new folder named `MMA891` in the current directory.

7. **Navigate to the Repository Folder:**

   - Change your current directory to the newly cloned repository by running:
     ```
     cd MMAI891
     ```

8. **Install Required Libraries:**

   - Now, install all the required libraries isted in the `requirements.txt` file using pip. Make sure you have Python and pip installed on your system. Run the following command:
     ```
     pip install -r requirements.txt
     ```
   - This command reads the `requirements.txt` file in the current directory and installs all the libraries listed there.

   - One of the library needed for this repo is spacy. Once spacy is installed you will have to download the NLP model separately by running the following code in your command line. You only have to do this once.
     ```
     python -m spacy download en_core_web_sm
     ```

8. **git pull:**

   - Labs will be updated continiously throughout the course. `requirements.txt` may also get updated several times. It is recommended that you run the following code before every class to ensure you have the most up to date repo and requirements.
     ```
     cd mmai891
     git pull
     conda activate mmai891
     pip install -r requirements.txt
     ```

## Data

For labs where a data file is needed, the data is stored in the respective folder. 

Thank you