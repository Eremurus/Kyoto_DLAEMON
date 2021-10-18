# DLAEMON
DLAEMON is a software program that can diagnose images of cherry leaves to see if they are diseased. Just upload the photo you took with your phone and press the Diagnose button to see the prediction of whether the leaf is diseased or not, and the confidence level of the prediction.
# DEMO
All you have to do is  just to upload the image and click on the "Diagnose" button.
For detailed instructions, see "tutorial_of_DLAEMON.docx".

# Requirement
* Users of mac

    Just double-click on DLAEMON/dist/dlaemon to use it.

* Non-mac users, or those who have had trouble with the above methods

    - Python3
    - Pillow
    - PyTorch
    - torchvision
    - numpy

# Installation
* If you are a non-mac user, or if the above method did not work for you, please run the following to install the necessary libraries, etc.
    - Download and install Python3 from https://www.python.org.
    - Type the following command on the command line to install Pillow.

    ```bash
    pip install Pillow
    ```
    - Type the following command on the command line to install PyTorch.
    ```bash
    pip install torch
    ```
    - Type the following command on the command line to install torchvision.
    ```bash
    pip install torchvision
    ```
    - Type the following command on the command line to install numpy.

    ```bash
    pip install numpy
    ```

 
# Usage
* Users of mac

    Double-click on NOBITA/dist/nobita to use it.
* If you are not a mac user, or if the above methods did not work for you


    Type the following command.
```bash
git clone https://github.com/igemsoftware2021/Kyoto_DLAEMON.git
cd Kyoto_DLAEMON/DLAEMON
python3 dlaemon.py
```
 
# Note
 
Only RGB images can be used; 4-channel images such as RGBA and black and white images cannot be used.
 
# License
DLAEMON is OSS. Everyone can use this software without any permission.

# Appendix
Kyoto_DLAEMON/Cherry_FineTuning.ipynb is the code used to build the AI in DLAEMON (the one that is doing the fine-tuning). Kyoto_DLAEMON/Cherry_CNN.ipynb is the code used to train the AI from the beginning using CNNs, using the same data set (see the software wiki for details). These files retain the output , including the learning curve and accuracy listed in the wiki. There is also text describing what part of the code is doing what.

# Author
 
* Producer : Kaho Tanaka
* Affiliation : Team:iGEM Kyoto 2021
* E-mail : igemkyoto2021@gmail.com
 