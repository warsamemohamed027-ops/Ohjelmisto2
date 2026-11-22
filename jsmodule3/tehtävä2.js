let participants = [];
let amount = Number(prompt("How many participants?"));

for (let i = 0; i < amount; i++) {
    let name = prompt("Enter participant name");
    participants.push(name);
}

participants.sort();

let list = document.getElementById("list");

for (let i = 0; i < participants.length; i++) {
    list.innerHTML += "<li>" + participants[i] + "</li>";
}