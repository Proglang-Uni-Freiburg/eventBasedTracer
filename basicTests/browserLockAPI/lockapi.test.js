function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms))
}

function promisedHttpRequest(url) {
    return new Promise((resolve, reject) => {
        var req = new XMLHttpRequest();
        req.addEventListener("load", () => {
            console.log(req);
            resolve(req.response)
        })
        req.open("GET", url)
        req.overrideMimeType("text/html");
        try {
            req.send();
        } catch (e) {
            reject(e);
        }
    })
}

var scriptStart = performance.now();

var display = document.getElementById("state");

display.innerHTML = "foo";

var lockA = navigator.locks.request("foo", async (lock) => {
    if (!lock) return;
    var req = await promisedHttpRequest("https://wttr.in/qfb?format=3");
    display.innerHTML = String(req);
    console.log(display);
})
var lockB = navigator.locks.request("foo", async (lock) => {
    if (!lock) return;
    await sleep(100);
    display.innerHTML += `<span>done sleeping</span>`
});


Promise.all([lockA, lockB]).then(() => {
    display.innerHTML += "<span>done</span>";
    var scriptEnd = performance.now();
    var difference = scriptEnd - scriptStart;
    console.log(`script took ${difference}ms`, scriptStart, scriptEnd, difference);
    display.innerHTML += `<span>script took ${difference}ms</span>`;
})
