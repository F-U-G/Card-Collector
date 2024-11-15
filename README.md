# Card Collector

Card Collector is a Python program using SQLite to keep track of Pokemon Cards. Card Collector is a terminal program that simply takes inputs in order to add, remove or view cards. This is my project for the CS50 final.

Every card has a unique ID but has a count associated with it, this means you can have duplicate cards as the same ID. This also means you can have two cards with the same name, which happens often with Pokemon cards. Each card also has a card number, this is on the bottom right of a card and is formatted like this: 0/67.

## Usage
Make sure you have the 'collection.db' file in the same folder as Card Collector. The following options are available:
- a - add a card
- r - remove a card
- d - display cards, leave blank to see all cards
- q - quit without saving
- sq - save and quit

To add a card you will enter the card name, set, number, type or color, and the amount of that card you have.

To remove a card simply search the card name, or press enter to see all cards, to see the card IDs. Enter the ID of the card to remove, then the count.

## Roadmap
- [ ] Add arguments for using separate databases
- [ ] Better ASCII UI
- [ ] Support for other tcg cards like MTG, Yu-Gi-Oh, etc
- [ ] Add a price column in the database table