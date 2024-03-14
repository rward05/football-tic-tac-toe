function toggle(element) {
    if (element.innerHTML) {
        element.innerHTML = ""
    } else {
        element.innerHTML = "<img src='/static/images/cross.svg' height='75px' title='Player 1 placed a Cross!'>"
    }
}