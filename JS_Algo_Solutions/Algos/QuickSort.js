 const partition = (arr,start,end) => {
    var pivot   = arr[Math.floor(arr.length / 2)], //middle element
        i       = start //left pointer
        j       = end; //right pointer
            while (i <= j) {
                while (arr[i] < pivot) {
                    i++;
                }
                while (arr[j] > pivot) {
                    j--;
                }
                if (i <= j) {
                    var temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;//swap two elements
                    i++;
                    j--;
                }
            }
            return j;
        }


const QSort = (arr,start,end) =>{
    if (start < end) 
        { 
            var psort = partition(arr,0,arr.length-1);
            QSort(arr, start, psort-1); 
            QSort(arr, psort+1, end); 
        } 
}
var newarr = [10,2,0,40,18,12,7];
console.log(QSort(newarr,0,newarr.length-1));

//attempt 2:

function partition(arr, low, high) {
    var mid = Math.floor((high + low) / 2);
    var pivot = arr[mid];
    while(low < high) {
      if(arr[low] < pivot) {
        low++;
      } else if(arr[high] > pivot) {
        high--;
      } else {
        [arr[high], arr[low]] = [arr[low], arr[high]];
      }
    }
    return low;
  }
  
  function quickSort(arr, low=0, high=arr.length-1) {
    if(low < high) {
      const pI = partition(arr, low, high);
      quickSort(arr, low, pI-1);
      quickSort(arr, pI+1, high);
    }
  }
  
  const arr = [4, 5, 2, 1, 3];
  quickSort(arr);
  console.log(arr);