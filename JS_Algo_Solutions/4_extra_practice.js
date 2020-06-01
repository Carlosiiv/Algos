// Many algorithms have multiple valid solutions.
// If you have time, try coming up with a different approach/solution for reversing an array

var arr = [8,6,7,5,3,0,9];
var result = [];
var i = null;
for (i = arr.length - 1; i >= 0; i -= 1)
{
    result.push(arr[i]);
}
console.log(result);

//another way

arr.reverse(arr);
console.log(arr);

