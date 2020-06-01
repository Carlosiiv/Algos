// Given an array, shift all values one position to the left.  Change the final position to 0. Return the changed array
// Predicted Output: shiftLeft([1,2,3,4,5]) should return [2,3,4,5,0];
function shiftLeft(arr){
    for ( var i = 0; i < arr.length; i++){
        arr[i] = arr[i + 1];

    }arr.pop();
     arr.push(0);
    return arr
    
} 
var resultArr = shiftLeft([1,2,3,4,5]);
// shiftLeft Test Cases:
var r1 =  shiftLeft([1,-7,2,-5,8,7,-11,10])        //Expected output: [-7,2,-5,8,7,-11,10,0]
var r2 =  shiftLeft(["hello","hi","yo","wazzup"])  //Expected output: [hi","yo","wazzup",0]
var r3 =  shiftLeft([1,2])                         //Expected output: [2,0]
var r4 =  shiftLeft([1])                           //Expected output: [0]
var r5 =  shiftLeft([])                            //Expected output: []
console.log(resultArr,r1,r2,r3,r4,r5);