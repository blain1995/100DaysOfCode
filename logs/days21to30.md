# Log of days 21 to 30

## Day 21: 21st March 2021

### Today's progress:

Today I have been learning a bit more about list comprehensions and dictionary comprehensions. I have learnt a little bit about these in the past, but have never really used them in practice. 

I updated my [states game](https://github.com/blain1995/100DaysOfCode/blob/main/scripts/days21to30/day21/states_updated/main.py) to optimise the code using a list comprehension. This replaced a four line for loop, shortening this down to just one line of code.

I also made a [nato phonetic alphabet word converter](https://github.com/blain1995/100DaysOfCode/blob/main/scripts/days21to30/day21/nato_alphabet/main.py) which loads in a csv containing the nato phonetic alphabet and converts this into a dictionary. The user is then asked for a word and then the program loops through the word and pulls out the corresponding value.

### Thoughts:

I enjoyed today, made me realise there are definitely times in the past where I should've maybe been using a list/dictionary comprehension instead of a for loop. I like how they make the code more concise and readable.

Excited to learn about tkinter tomorrow :)

## Day 22: 22nd March 2021

### Today's progress

Today I have been learning about Tkinter, and have been playing around with some basic gui programs.

I made my own [miles to km converter](https://github.com/blain1995/100DaysOfCode/blob/main/scripts/days21to30/day22/day22_miles_to_km.py) it's quite basic but I'm happy that I can do stuff like this now! Excited to build more programs which utilise gui's in the future.

### Thoughts:

Found today fairly straight forward, although this was definitely a bit of a step up from the turtle programs I have been making. Excited for more of this tomorrow :)

## Day 23: 23rd March 2021

### Today's progress:

Today I made a [pomodoro timer](https://github.com/blain1995/100DaysOfCode/blob/main/scripts/days21to30/day23/day23_pomodoro.py) using my new Tkinter skills

### Thoughts:

Feeling a bit more confident with Tkinter now, enjoyed this project and can actually see myself using this regularly.

## Day 24: 24th March 2021

### Today's progress:

Today I made a [password manager](https://github.com/blain1995/100DaysOfCode/blob/main/scripts/days21to30/day24/day24_password_manager.py) GUI program which exports inputted passwords to a [data.txt file](https://github.com/blain1995/100DaysOfCode/blob/main/scripts/days21to30/day24/data.txt) for storage. Spoilers the example file contains fake email and passwords!

The program can also generate a password for you if you're feeling particularly uncreative.

### Thoughts:

Nice little program, I enjoyed making this. Impressed with Tkinters broad range of functions but a little dissapointed in the terrible documentation!

## Day 25: 25th March 2021

### Today's progress:

Today I learnt about try/except/else/finally statements and also about the use of JSON data. 

I then went back to my [nato alphabet script](https://github.com/blain1995/100DaysOfCode/blob/main/scripts/days21to30/day25/nato/main.py) to include a KeyError if the user enters any non-alphabetical characters into the program.

I also went back and updated my [password manager](https://github.com/blain1995/100DaysOfCode/blob/main/scripts/days21to30/day25/pass_manager/day25_password_manager.py) which now has except statments for KeyErrors and FileNotFoundErrors. I have also switched the data storing format to JSON. 

finally I added a search function where you can search the JSON file and fetch the relevent password and email used for that website.

### Thoughts:

Found today pretty straight forward, I'm enjoying going back to previous scripts to increase the functionality of my code.

## Day 26: 26th March 2021

### Today's progress:

Today was a capstone project using Tkinter and pandas. I made a [flash card app](https://github.com/blain1995/100DaysOfCode/blob/main/scripts/days21to30/day26/main.py) which tests your knowledge of french words. If the user knows the english translation, they should click the tick button, at which point this word is removed from the pool of random french words.

### Thoughts:

This was challenging but good, really enjoying making more GUI programs, as this is not something I do day to day when I use python for work.

## Day 27: 27th March 2021

### Today's progress:

Did a lot of coding today! Played around with sending emails using smtplib and APIs to make a few projects, see below:

[motivational quote email script](https://github.com/blain1995/100DaysOfCode/blob/main/scripts/days21to30/day27/motivation/day27_motivation.py)

[birthday email sending app](https://github.com/blain1995/100DaysOfCode/blob/main/scripts/days21to30/day27/birthday/main.py)

[Kanye quote generator](https://github.com/blain1995/100DaysOfCode/blob/main/scripts/days21to30/day27/Kanye_quotes/main.py)

[International Space Station Tracker](https://github.com/blain1995/100DaysOfCode/blob/main/scripts/days21to30/day27/ISS/day27_ISS_tracker.py) that emails you when the ISS is overhead

### Thoughts:

Really enjoyed today! I've used APIs once or twice in the past but I feel like this was a nice little refresh and I'm excited to use my API & SMTP skills in the future!

## Day 28: 28th March 2021

### Today's progress:

Today I revamped my previous in-console quiz, it now has a GUI using Tkinter, and uses an API to generate new questions everytime.

All the scripts can be found [here](https://github.com/blain1995/100DaysOfCode/blob/main/scripts/days21to30/day28)

### Thoughts:

I enjoyed going back and improving a previous project. I am definitely feeling a bit more competent with python!

## Day 29: 29th March 2021

### Today's progress:

Today I made a script which uses the [Open Weather Map API](https://openweathermap.org/api) and [Twillio](https://www.twilio.com/) to determine whether it will rain in my area in the next 12 hours and if so, will text me to tell me to bring an umbrella.

The full code is [here](https://github.com/blain1995/100DaysOfCode/blob/main/scripts/days21to30/day29/day29_main.py)

### Thoughts:

This is actually really useful, I have uploaded my code to [Python Anywhere](https://www.pythonanywhere.com/) and set it to run every day at 7am!

Really enjoyed today's project :) 

## Day 30: 30th March 2021

### Today's progress:

Today I wrote a script which checks the end of day stock price for a company (as an example I used Tesla) on the last two days of trade, works out what the percentage difference between stock price is at close on those days. If the stock price fluctuates by more than 5% then I recieve the latest 3 news stories about the company as seperate texts.

The script can be found [here](https://github.com/blain1995/100DaysOfCode/blob/main/scripts/days21to30/day30/main.py)

### Thoughts:

I enjoyed this project, solved this with minimal googling of error messages which I was happy with. Feel like APIs are fairly simple now I am a bit more used to them!
