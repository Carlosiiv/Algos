const words = [
    ["quick", "lazy"],
    ["brown", "grey", "red"],
    ["fox", "dog"]
];

let i = 0;
let combs = words[i];

while(i++ < words.length-1){
    let new_combs = [];
    for(let comb of combs){
        for(let word of words[i]){
            new_combs.push(comb + " " + word);
        }
    }
    combs = new_combs;
}

console.log(combs);