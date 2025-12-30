# KATTYKAKES FOCUS TIMER
#### Video Demo:  https://youtu.be/rwYg3awNv7U
#### Description:

This is a web-based app written in Python (using the Flask framework) and heavily utilizing JavaScript on the client side. The app is a focus timer that can help you stay focused on your work by disincentivizing distractions.

##### Overview

The app's core functionality is contained in three features: a slider that allows you, the user, to select a length of time to focus, a display that counts down the remaining focus time, and a reward/penalty mechanism that encourages you not to click away from the app (i.e., lose focus). The slider can be set to any value between 5 and 120 minutes, at 5-minute increments. I chose these parameters for practicality's sake - anything below 5 minutes is too short for a focus session, anything above 120 is likely too long, and 1-minute increments would make the slider too fiddly. Once you set a session length and click the Start button, the session begins: the Start button becomes a Cancel button, all other buttons on the page are disabled, and the penalty mechanism is enabled. If you click another tab or minimize the window, the session ends early and no reward is earned. On the other hand, if the timer is allowed to reach zero (i.e., you stay focused the whole time), then there's a reward - cookies!

*Wait, why are there cookies?* 

Because there's a cat who bakes them, of course! This app isn't called KattyKakes for nothing. The star of the show is Muffin, your friendly neighborhood kitty baker! The app shows Muffin standing in a cute (but bare - more on that later) kitchen. When you starts a focus session, Muffin starts mixing up some delicious cookie batter. Once the focus session ends, you are rewarded with cookies (the exact number of cookies depends on the focus session length - you earn one cookie for every 5 minutes), courtesy of Muffin. If you lose focus, a modal window appears, showing that Muffin has gone to sleep - hence, no cookies. After a completed session, you have the option to start a five-minute break timer. During the break, you can play one or more rounds of Tic-Tac-Toe with Muffin (or none, if you prefer to do something else during the break). I chose Tic-Tac-Toe for two reasons: first, it's a quick game to play, so there's no danger of the game lasting longer than the five minutes. Second, I knew it would be [challenging to code](#javascript). In the future, I'd like to add a couple more game options, like Hangman and Battleship, that are equally quick to play and challenging to implement.

*Tell me more about the cookies!*

Virtual cookies are great, but unless there's something that can be done with them, they're not a very compelling incentive. That's why the app includes a shop where you can use cookies to buy decor for the initially bare kitchen. There are items to decorate the walls, counters, window, shelves, and floor. Each item has an associated cost, ranging from 10 to 100 cookies (prices were set based on how "fancy" I thought each item looked). These are pretty steep, considering it takes five minutes of focus time to earn 1 cookie. This was a deliberate decision on my part - the point of the focus timer is to *focus*, not to buy cute things for the kitchen. The high prices encourage more focus sessions while providing long-term goals to look forward to.

Speaking of cookies, the app uses browser cookies to remember how many (virtual) cookies you have, and which decor items you already own (and it updates the background image of the kitchen to include the appropriate items - more on that in [the next section](#javascript)). Of course, this means you could simply edit the cookies to give yourself infinite (virtual) cookies and buy all the shop items in one go, but... Come on, where's the fun in that?

##### Key Components
###### Modals

This is, at its core, a very simple app with a very simple functionality. Thus it has only a single page (displaying the cat and the timer), with all of the extra content being displayed in modals. Modals are typically seen as undesirable UI features because they force the user into taking certain actions, but for my purposes, that is exactly what I wanted to do. The app does one thing, and one thing only. Any other content is extra - frosting, sprinkles, and a cherry on top - so when the user views that extra content, it's meant to be temporary. It's a supporting act, and each modal forces the user to intentionally close it to get back to the main event.

There are modals both within and outside of the focus session flow. Modals within focus session flow include:
- Confirm timer cancellation (to end the session early)
- Begin a 5-minute break after session completion
- Play Tic-Tac-Toe during the break
- Begin a new session after break is over
- Show sleeping cat when session is interrupted

Modals outside the session flow:
- Shop
- Info/instructions

###### JavaScript

The app makes extensive use of JavaScript to provide the vast majority of its functionality. I started this project with next to no JavaScript experience, so this proved quite the challenge. What follows is a brief summary of the JavaScript-powered features of the app.

- *Animated cat image* - Anytime Muffin is onscreen, rather than displaying a static image, setInterval() is used to alternate between two nearly identical images, creating a very simple animation. 
- *Browser cookies* - The document.cookie element is used to get and set cookie values for number of (virtual) cookies and decor items owned.
- *Update background image* - Each decor item has an associated image, *[item_name]_bg.png*, that shows the item in its correct position relative to the kitchen background, with a transparent background. When the app is refreshed, the app fetches the browser cookie to get a list of all currently owned items, then updates the document.body.style.backgroundImage element so that it layers all of their individual *XX_bg.png* images on top of the *kitchen.png* image - this way you'll see your kitchen with exactly the items you've already purchased.
- *Shop* - When the shop is open, the purchase buttons for each item change depending on whether the item is owned or not, and whether you can currently afford it or not. If the item is already owned, the button is grey and disabled. If you don't own the item yet but don't have enough cookies at the moment, the button is red and disabled. If you can afford to buy it, the button is blue and enabled. Clicking a blue button instantly updates the number of cookies available and changes all the item purchase buttons accordingly. Closing the shop also refreshes the page so that the background image updates to show newly purchased items.
- *Countdown timer* - During a focus or break session, setInterval() is used to update the remaining time displayed on the timer every second.
- *Focus session* - Starting a focus session does the following: the appearance and functionality of the Start button changes, all other buttons on the page are disabled, and an event listener is used to detect when the document's visibility attribute changes and interrupt the session.
- *Tic-Tac-Toe* - By far the most complex and challenging piece of this entire thing. First, the board is drawn on a canvas element. When the player selects X or O, the game starts, with X playing first. The player and computer take turns playing rounds. Each round is played via an asynchronous function that waits for certain actions to be completed before checking whether the endgame state has been met. During the player's turns, the asynchronous function waits for the player to click on an open space in the board, which then populates with the player's symbol. During the computer's turns, the asynchronous function waits for the computer to randomly select one of the open spaces, which then populates with the computer's symbol. After each round, the game checks for an endgame state (three-in-a-row or all squares filled). If the endgame condition has been met, the game is over and the game declares a winner or draw. If the endgame condition has not been met, the game continues to the next round.

##### Project Files

- app.py - Contains the Flask app configuration
- helpers.py - Contains a list of dictionaries with information for kitchen decor items, including item name, cost, image source file, and whether it overlaps with any other images
- templates/layout.html - Basic app layout. Includes default background image and header
- templates/index.html - Contains most of the app content. Includes cat images, modals, countdown timer. Also includes all of the JavaScript necessary to make the app function.
- static/styles.css - Custom styles. Primarily contains styles for elements in fixed positions (e.g., modal launch buttons)
- static/images/ - Contains all images for the app. Kitchen background, cat animations, cookies, and all decor items (both item-only images for the shop as well as transparent background images for layering)

##### Attribution

The artwork (Muffin and the kitchen) was made by me in Canva. I'm no artist, a fact which I believe worked in my favor here. The cute, simplistic art style enhances the app's focus functionality rather than distracting from it (at least, that's what I tell myself). The images of cookies and kitchen decor items all came from Canva as well. 
