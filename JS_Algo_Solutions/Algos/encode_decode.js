function encode(str){
    let newStr=' ';
    let count=1;
    for (let i=0; i<str.length; i++ ){
      while(str[i]===str[i+1]){
        count+=1;
        i++;  
      } 
      newStr+=str[i]+count;
      count = 1;
    }
    return newStr;
  }
  console.log(encode('aaabbbccdd'))
  
  function decode(str){
    let newStr='';
    for(let i=0; i<str.length; i+=2){
      if(isNaN(str[i])){
        newStr+=str[i]
        let x = parseInt(str[i+1])
        for(var j=1;j<x;j++){
          newStr+=str[i];
        }
      }
    }
    return newStr
  }
  console.log(decode('a3b3c2d2'))