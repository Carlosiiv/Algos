function InsertSort(arr){
    var len = arr.length;
    for(var i = 0; i < len ; i++){
        var  idx = arr[i];
        var j = i - 1;
        while(j >= 0 && arr[j] > idx){
            arr[j+1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = idx;
    }
    return arr;
}
var test = [10,1,5,2,12,16,3];
console.log(InsertSort(test));
// =========================================
const insertSort = (arr) => {
    for(let i = 1; i < arr.length; i++){
        let j = i;
        while(j > 0 && arr[j] < arr[j-1]){
            [arr[j], arr[j-1]] = [arr[j-1], arr[j]]
            j--;
        }
    }
    return arr;
}

var newarr = [10,1,20,4,3,0,12];
console.log(insertSort(newarr));