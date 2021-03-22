let cards = document.getElementsByClassName('card__inner');
cards = [...cards]
let clickCount = 0;
cards.forEach((card) => {
    card.addEventListener('click', function () {
        console.log('click')
        console.log(clickCount)
        card.classList.toggle('is-flipped');
        clickCount +=1;
        if (clickCount === 2) {
            card.classList.add('done-flipping')
        }
        
        

    /*// memoize the click count
// if click count = 2
	// add a new class name to the card ex: “done-flipping” (or whatever)
	// in main.css: add styles for done flipping:
	// left: 200px */

    });
} )