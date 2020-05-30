function hash(key) {
    let output = 0;
    for(let i=0; i<key.length; i++) {
        output += key.charCodeAt(i);
    }
    return output;
}

class HashMap {
    constructor(cap = 10) {
        this.capacity = cap;
        this.hashmap = [];
        for(let i=0; i<this.capacity; i++) {
            this.hashmap.push([]);
        }
    }
    put(key, value) {
        var x = hash(key)
      var y = x % this.capacity;
      if( this.hashmap[y].hasOwnProperty(key)){
        this.hashmap[y][key] = value
      }else{
        this.hashmap[y].push({key: value})
      }
      return(this);
    
    }
    get(key) {
        let index = hash(key) % this.capacity;
        for(let i = 0; i < this.hashmap[index].length; i++){
            if(this.hashmap[index][i] === key){
                return this.hashmap[index][i+1];
            }
        }
        throw new Error(`the key ${key} was not present!`)
    }
}

let hm= new HashMap(10)
hm.put("fruit", "apple");
hm.put("fruit", "pear");
hm.put("vegetable", "carrot");
console.log(hm)