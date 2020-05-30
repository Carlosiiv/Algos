const rotateStr = (str,num) => {
    num %= str.length;
    var str2 = "";
    var size = str.length - num;
    var i = 0;
    var temp = str.slice(-num);
    var str2 = temp;
    while( i < size){
        str2 += str[i];
        i++
    }
    
    return str2;
}
console.log(rotateStr("Hello", 1000));

// implementation 2

function rotateString(str,num){
    num %= str.length;
    var arr = str.split("");
    for(let i = 0; i < num; i++){
        arr.unshift(arr.pop());
    }
    return arr.join("");
}
console.log(rotateString("Hello World",50004));

const isRotation = (str1,str2) => {
    if(str1.length !== str2.length){
        return false;
    }
    for(let i = 0; i <str1.length; i++){
        if(str1 === rotateString(str2,i)){
            return true;
        }
    }
    return false;
}

console.log(isRotation("Bingo","ingtB"));