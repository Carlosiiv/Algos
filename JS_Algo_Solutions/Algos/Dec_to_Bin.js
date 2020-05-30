function bitStrToDec(b){
    let i = b.length - 1;
    let num = 0;
    let pow = 0;
    while (b[i] !== "b"){
      num += Math.pow(2,pow) * b[i];
      pow++;
      i --;
    }
    return num;
  }
  bitStrToDec("0b1010101");
  bitStrToDec("0b11110011");
  
  function decToBin(num){
      let strBit = "";
      while(num > 0){
          num /= 2;
          let rem = num - Math.floor(num);
          if(rem > 0){
              strBit = "1" + strBit;
          }
          else{
              strBit = "0" + strBit;
          }
          num = Math.floor(num);
      }
      return "0b" + strBit;
  }
  
  console.log(decToBin(255));











