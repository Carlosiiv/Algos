function bubblesort(arr){
    var len = arr.Length;
    for (var i=0; i<len; i++){
        for (var j=0; j<len-i; j++){
            if (arr[j] > arr[j+1]){
                var temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
console.log(arr);
}
var anArray = [2,10,20,1,5]
bubblesort(anArray);
