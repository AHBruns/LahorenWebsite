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

function type_names() {
    console.log("upadting name");
    let el = document.getElementById("Alex_Bruns_Label");
    el.innerText = "Alex Bruns: " + names[names_idx % names.length];
    names_idx++;
}

window.onload = function () {
    setInterval("type_names()", 1000)
};