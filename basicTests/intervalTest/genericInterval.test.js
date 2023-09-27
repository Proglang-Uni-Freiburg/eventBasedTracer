let time = 0;
const element = document.getElementById("foo");

setInterval(() => {
    time += 1;
    element.innerHTML = time.toString();
    }, 100);
