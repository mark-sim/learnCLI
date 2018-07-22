
# LearnCLI : A command line tool for [Learn](https://learn.uwaterloo.ca)

LearnCLI is a python application that allows you to access [Learn](https://learn.uwaterloo.ca) from a command line. It's easy to view your grades (including feedbacks) and you can also download course contents. Additionally, LearnCLI can be used to automatically download course contents and drop it to your Dropbox.

## Requirements
* [python](https://www.python.org/getit/) (3+)
* [Google Chrome](https://www.google.com/chrome/)
* [Dropbox Account](https://www.dropbox.com/h) (optional)

## Installation
Clone this repository then run
```
python setup.py install
```
from the root repository.

## Configuration
There are some required configuration if you want to use the Dropbox feature.
#### Dropbox Access Token
* Go to [Dropbox Developers](https://www.dropbox.com/developers/apps) and get your access token. 
More information can be found [here](https://blogs.dropbox.com/developers/2014/05/generate-an-access-token-for-your-own-account/)
* Copy and paste the access token to ```/d2d.auth```

#### Download Directory
* Set ```download.default_directory = AnyDownloadDirectoryFullPath``` in ```/d2d.config```

## Usage
Go to /src/ directory then run:
```
python -W ignore __main__.py -u username -p password
```
#### List of Available Commands in CLI
|    **Parameters**    |    **Description**       |
|:--------------------:|:------------------------:|
| **h**   | help       |
| **q**      | quit      |
| **ls**    | list all files in current directory     | 
| **cd**   | change directory  |
| **d2d**  | downloads specified file and drops it to your dropbox (Regex supported) |

#### Example:
```
python -W ignore __main__.py -u username -p password

Logging in to https://learn.uwaterloo.ca
Logged in.

List of available commands:
- h: help
- q: quit
- ls: list all files in current directory
- cd: change directory
- d2d: downloads specified file and drops it to your dropbox (Regex supported)
       
List of all the courses:
- Math Undergraduate Students
- PD 8 Online - Spring 2018 – 081/082/083
- WKRPT 300M - Spring 2018

>>> cd PD 8 Online - Spring 2018 – 081/082/083
>>> ls

Files in current directory:
- Content
- Grades

>>> cd Grades
-------------------------------------------------
Assignment 1
18 / 20
18 / 20
90 %
Individual Feedback
Good start Sung! You included some important factors contributing to intercultural differences and biases. However, you needed to include more detail and explanation to make your response stronger. Be sure to include references where needed, Step 1 in this case, to relate to the course content. For step 2, you pointed out some very relevant assumption made through cultural biases. Including more detail to your response would of the methods to avoid these biases would have made your answers more wholesome.
-------------------------------------------------
Assignment 2
16 / 20
16 / 20
80 %
Individual Feedback
Great start Sung! You included some interesting aspects of your family values which needed to be elaborated upn in Part 1 of your response. You included a good example for Question 3 in part 1 but more detail was required to receive full marks. For part 2, you included some relevant ideas and concepts but a stronger explanation and connection to the course content was required. Also you did not mention which two questions you were answering to.
-------------------------------------------------
...
>>> cd ..
>>> cd ..
>>> cd Math Undergraduate Students
>>> cd Content
>>> ls

Files in current directory:
- ACTSC Waitlist
- 201213PROGRAMBrochure-1-acting
- SuccessCoachingWorkshopsWinter2014
- TutorConnectPoster-2
- StudySessionsPosterWinter2014
- exam drop-in Math TC

>>> d2d ^S*
Dropping C:/Users/USER/Desktop/temp/SuccessCoachingWorkshopsWinter2014.pdf to Dropbox
Dropped C:/Users/USER/Desktop/temp/SuccessCoachingWorkshopsWinter2014.pdf to Dropbox
Dropping C:/Users/USER/Desktop/temp/StudySessionsPosterWinter2014.pdf to Dropbox
Dropped C:/Users/USER/Desktop/temp/StudySessionsPosterWinter2014.pdf to Dropbox
```