let names = [
    "Solidity Dev",
    "Python Script Kiddie",
    "Blockchain Engineer",
    "Software Engineer",
    "Language Designer",
    "Computer Scientist",
    "Researcher",
    "Stack Overflow Member",
    "Coffee Consumer"
];
let names_idx = 0;
let angle = 0;
let zoom = 1;
let tick = 1;

function type_names() {
    console.log("updating name");
    let el = document.getElementById("Alex_Bruns_Label");
    el.innerText = "Alex Bruns: " + names[names_idx % names.length];
    names_idx++;
}


var boxMullerRandom = (function () {
    var phase = 0,
        RAND_MAX,
        array,
        random,
        x1, x2, w, z;

    if (crypto && typeof crypto.getRandomValues === 'function') {
        RAND_MAX = Math.pow(2, 32) - 1;
        array = new Uint32Array(1);
        random = function () {
            crypto.getRandomValues(array);

            return array[0] / RAND_MAX;
        };
    } else {
        random = Math.random;
    }

    return function () {
        if (!phase) {
            do {
                x1 = 2.0 * random() - 1.0;
                x2 = 2.0 * random() - 1.0;
                w = x1 * x1 + x2 * x2;
            } while (w >= 1.0);

            w = Math.sqrt((-2.0 * Math.log(w)) / w);
            z = x1 * w;
        } else {
            z = x2 * w;
        }

        phase ^= 1;

        return z;
    }
}());

let v = 0;
let t = 0;

function randomWalk(steps, randFunc) {
    steps = steps >>> 0 || 100;
    if (typeof randFunc !== 'function') {
        randFunc = boxMullerRandom;
    }

    var points = [],
        value = 0,
        t;



    return points;
}

function random_transform() {
    let e = document.getElementById("page");
    v += (boxMullerRandom() / 10000.0);
    // angle = v*360;
    zoom = zoom / (1 + (v/100) + (tick/10000000));
    console.log(v);
    tick++;
    e.style.transform = "rotate(" + angle.toString() + "deg) " + "scale(" + zoom.toString() +")";


}

window.onload = function () {
    // setTimeout("setInterval(\"random_transform()\", 1)", 5000);
    setInterval("type_names()", 1000);
};