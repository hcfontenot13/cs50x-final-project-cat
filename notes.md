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
3. Test here
