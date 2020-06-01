// Given var arr = [10,3,6,9,4,13]
// change all numbers 10 or higher to "Big" and change numbers 5 or smaller to "Small" and print the result 
// Predicted output: ["Big","Small",6,9,"Small","Big"]
// When you have solved this, create new values for your array and ensure it still works as expected.

var arr = [10,3,6,9,4,13];
for( var i = 0; i < arr.length; i++){
    if( arr[i] >= 10){
        arr[i] = 'Big';
    }
        
    if(arr[i] <= 5){
        arr[i] = 'Small';
    }
}
console.log(arr);