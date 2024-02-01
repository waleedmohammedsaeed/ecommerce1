const scroller = document.querySelector('.scroller')
if (!window.matchMedia("(prefers-reduced-motion: reduce)").matched){
	addAnimation();
}

function addAnimation () {
		scroller.setAttribute("data-animated", true)

		const scrollInner = document.querySelector('.scroller-inner')
		const scrollerContent = Array.from(scrollInner.children);
		
		scrollerContent.forEach(item => {
			const duplicatedItem = item.cloneNode(true)
			duplicatedItem.setAttribute("aria-hidden", true)
			scrollInner.appendChild(duplicatedItem)
		});
}