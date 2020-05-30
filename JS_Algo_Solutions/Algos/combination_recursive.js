function allCombs(words) {

    var results = [];
  
    function helper(comb, i) {
  
      if(i === words.length) {
        results.push(comb);
      } else {
        for(var j=0; j<words[i].length; j++){
          helper(comb + words[i][j] + " ", i+1);
        }
      }
  
    }
    helper("", 0)
    return results;
  }
  
  allCombs([
      ["quick", "lazy"],
      ["brown", "red", "grey"],
      ["fox", "dog"]
  ]);