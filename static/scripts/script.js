// Function to toggle the content of an element
function toggle(element) {
    // Check if the element already has innerHTML content
    if (element.innerHTML) {
        // If it does, clear the innerHTML content
        element.innerHTML = "";
    } else {
        // If it doesn't, set innerHTML to include an image of a cross
        element.innerHTML =
            "<img src='/static/images/cross.svg' height='75px' title='Player 1 placed a Cross!'>";
    }
}
