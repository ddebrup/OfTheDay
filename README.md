# OfTheDay
A program solely written in python language, aimed at reminding people to wish to, on their respective (pre-added) birthdates.

## Procedure

Clone the repo<br>
~ git clone "https://github.com/ddebrup/OfTheDay.git"<br>
<br>
Run the following script in bash over the cloned directory<br>
> Install all dependencies
```
pip install -r requirements.txt
```
> Running the script
~ nohup python main.py &<br>
The above code makes the code run as a daemon service for a session (intend to add script to make it run solely as an independent service in the background automatically after boot)<br>
<br>
The code starts running in the background as a service <br>
The keyboard gets listened to, as and when a given key combination gets pressed, the following demonstrated feature gets into working.<br>

### Working on
~ A solely independent daemon service firing up the program automatically upon computer wake up<br>
~ Customised time based push notifier<br>
~ Customised push email based notification services<br>
~ Much more coming up, Stay tuned!<br>

#### A remark on the code efficiency
~ The code seems out not to be much efficient for computers with RAM lesser than 4GB<br>
~ Emphasis to be given for making the code as efficient as possible, to let it run in the background without much memory consumption
