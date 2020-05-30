

function mergeArrays(arr1, arr2){
    let newArr=[];
    var i = 0;
    var j = 0;
    while(newArr.length != (arr1.length+arr2.length)){
      if(arr1[i] < arr2[j]){
          if(arr1[i] === undefined){
            newArr.push(arr2[j]);
            j++
          }else{
            newArr.push(arr1[i]);
            i++;  
          }
      }
      else{
          if(arr2[j] === undefined){
            newArr.push(arr1[i]);
            i++
          }else{
            newArr.push(arr2[j]);
            j++; 
          }
      }
    }
    return newArr;
  }
  
  console.log(mergeArrays([10,20,30] , [2,4,6,8,10,11]));