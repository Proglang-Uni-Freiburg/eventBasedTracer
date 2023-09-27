var coolString = "";

function repeatNTimes(callback, delay, iterations){
    var i = 0;
    var interval = setInterval(() => {
        callback();
        if (++i >= iterations) clearInterval(interval);
    }, delay)
}
repeatNTimes(() => {
    coolString += "a";
}, 1, 1000);