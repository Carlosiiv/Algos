const Intersect = (arr1, arr2) =>{
    var newArr = [];
    var n = arr1.length;
    var n2 = arr2.length;
    var i = 0;
    var j = 0
    while( i < n && j < n2){
        if(arr1[i] === arr2[j]){
            newArr.push(arr1[i]);
            i++;
            j++;
        }
        else if(arr1[i] < arr2[j]){
            i++
        }
        else{
            j++
        }
    }return newArr;
}
console.log(Intersect([2,4,5,7],[2,2,7]));