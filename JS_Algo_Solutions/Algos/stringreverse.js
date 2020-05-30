stringToArray = (str) => {
    var newArr = [];
    var newStr = "";
    var i = 0;
    console.log(str[i]);
    while( i < str.length){
        if(str[i] === " " && str[i+1] !== " "){
            newArr.push(newStr);
            newStr = "";
            i++;
        }else{
            newStr += str[i];
            i++;
        }
    }
    newArr.push(newStr);
    return newArr;
}

console.log(stringToArray("My  Name Is Carlos"));

arrayToReverseStr = (arr) => {
    var newStr = "";
    var temp = 0;
    var mid = Math.floor(arr.length/2);
    for( var i = 0; i < mid; i++){
        temp = arr[0+i];
        arr[0+i] = arr[arr.length - 1 - i];
        arr[arr.length - 1 - i] = temp;
    }
    for(var j = 0; j < arr.length; j++){
        newStr += arr[j];
        newStr += " ";
    }

    return newStr
}
console.log(arrayToReverseStr(stringToArray("My Name Is Carlos")));
