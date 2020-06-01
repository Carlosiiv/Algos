// given some number, print "adding up" to the console and add from 1 up to that numnber and return the sum
// Predcted output: sigma(5) should return 15   (I.E: 1+2+3+4+5 =15)

function sigma(num){
    var s = 0;
    for( var i = 0; i <= num;i++){
        s += i;
    }
    return s;
}
var sum = sigma(5);                                //Expected output: 15
var ta = sigma(10);                                //Expected output: 55
var tb = sigma(1);                                 //Expected output: 1
var tc = sigma(0);                                 //Expected output: 0
var td = sigma(-10);                               //Expected output: 0
console.log(sum, ta,tb,tc,td);
