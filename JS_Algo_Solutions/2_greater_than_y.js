// Given an array and a number y, count and return how many numbers in the array are bigger than y.
// Predcted output: greaterThanY([1,6,8,3,5,2], 4) should return 3

function greaterThanY(arr, y){
    var h = 0
    for ( var i = 0; i < arr.length; i++){
        if( arr[i] > y){
            h++
        }
    } return h;
}
var result = greaterThanY([1,6,8,3,5,2], 4);
// greaterThanY Test Cases:
var result1 = greaterThanY([5,6,7,8,9,10], 4)          //Expected output: 6
var result2 = greaterThanY([5,6,7,8,9,10], 12)         //Expected output: 0
var result3 = greaterThanY([1,6,8,3,5,2], -5)          //Expected output: 6
var result4 = greaterThanY([-2,-6,-8,-3,-5,-2], -4)    //Expected output: 3
var result5 = greaterThanY([], 5)                      //Expected output: 0
console.log(result, result1, result2, result3, result4, result5);
