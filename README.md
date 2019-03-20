# Iwen

Colour palette creator for Swift and Android from Adobbe XD file. 

Iwen gets colours and its names from Addobe XD assets section and make colour palettes
for both Android and Swift developers.

For **Android** it will create standard XML file and for **Swift** it will create 
.xcassets palette with swift code to help using colours in code. Also, if you use 
Iwen on MacOS it will additionally create .clr file (if you have Swift installed) 
which you can move to ``~/Library/Colors`` folder and start using that type of palette.

### Prerequisites
You will need to install:
* Python 3.x
* Swift (for MacOS)

### Installation of prerequisites 

#### Windows

To download *Python* [click here](https://www.python.org/downloads/release) 

Be sure to check "**Add Python to PATH**" when installing.

After successful installation go to *Control Panel* -> *System* -> 
*Advanced system settings* (on left side menu) -> *Environment Variables*

In *System variables* click on **Path** and click **Edit**

Click **New** to add new variable and put python installation path (in my case it was C:\Users\my_username\AppData\Local\Programs\Python\Python37)

### MacOS

For MacOS just make sure your Python is up to date - to have version 3.x 

Additionally you can install Xcode to get Swift language. 
To install it [click here](https://itunes.apple.com/us/app/xcode/id497799835)

## Installing and Running

Download the project to your computer and extract it. Open terminal (or cmd) 
and navigate to that folder. 
To navigate to your project type in terminal:
```cd path_to_iwen_folder ```

After that run project with command ```python main.py ```



## Author

* **Ljubo Maricevic**  

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
