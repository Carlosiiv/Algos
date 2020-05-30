const hexidecimal = {
  '0' : 0,
  '1' : 1,
  '2' : 2,
  '3' : 3,
  '4' : 4,
  '5' : 5,
  '6' : 6,
  '7' : 7,
  '8' : 8,
  '9' : 9,
  'a' : 10,
  'b' : 11,
  'c' : 12,
  'd' : 13,
  'e' : 14,
  'f' : 15
}

function hex2dec(hex) {
  let result = 0;
  for ( let i = hex.length-1, pv = 0; i>1; i--, pv++) {
    // console.log(result)
    result += Math.pow(16, pv) * hexidecimal[ hex[i] ];
  }
  return result;
}

const getHex = "0123456789abcdef";


function dec2hex(dec) {
  let result = "0x";
  let pv = Math.floor(Math.log(dec)/Math.log(16));
  while(pv >= 0) {
    let x = Math.floor(dec/Math.pow(16, pv));
    dec %= Math.pow(16, pv);
    console.log(x);
    result += getHex[x];
    pv--;
  }
  return result;
}

console.log(dec2hex(300));

console.log(hex2dec('0x12c'))