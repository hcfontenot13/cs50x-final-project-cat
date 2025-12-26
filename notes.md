# Cat Focus Timer

## Functionality
You can set a focus timer and while it's counting down, there is a cat baking stuff.
If you click away from the tab, the cat goes to sleep and nothing gets baked.
After the timer ends, you can set a 5-minute break timer and play with the cat.
You can also sell the baked goods to buy things for the kitchen.

## Implementation
1. Timer
- Use JS to update "time remaining" display every second
- Use buttons to increase/decrease in 5-min intervals
- Min: 5, Max: 60
2. Focus
- JS: document.visibilityState, visibilitychange event

## Features to add
- [ ] Breaktime: Hangman?
- [ ] Breaktime: Battleship?
- [x] Sleep modal: sleeping cat images
- [x] Focus session: baking cat images
- [x] Change type/amount of stuff baked based on duration of session
- [x] Better kitchen image
- [ ] Toggle focus feature?
- [x] Info button
- [x] Store: sell baked goods, buy decorations
- [x] Use cookies to remember owned decorations
- [x] How to display different decorations?
- [ ] About page?
- [ ] Buy and pick kitchen color schemes?

## TODO
- [x] Add to info modal (acknowledge CS50)
- [x] Replace debugging defaults w/ production values (focus length, break length, decor prices)
- [x] Host the app
- [ ] Make video 
- [ ] Write ReadMe
- [ ] Submit
