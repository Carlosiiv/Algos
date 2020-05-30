function selSort(arr){
    var len = arr.length;
    for(var i = 0; i < len -1; i++){
        var min = i;
        for( var j = i + 1; j < len; j++){
            if( arr[j] < arr[min]){
                min = j;
            }
        }
        var temp = arr[min];
        arr[min] = arr[i];
        arr[i] = temp;
    }
    console.log(arr);
}
var arr = [2,10,20,1,5];
selSort(arr);

