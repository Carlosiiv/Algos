class MinHeap {
    constructor () {
      this.heap = [null]
    }
  
    traverse () {
      let child = this.heap.length-1;
      while(child > 1){
        let parent = Math.floor(child/2)
        if(this.heap[child] < this.heap[parent]) {
          [this.heap[child], this.heap[parent]] = [this.heap[parent], this.heap[child]];
          child = parent
        }
        else{
          return this;
        }
      }
      return this;
    }
  
    insert (value) {
      this.heap.push(value)
      this.traverse();
      return this;
    }
  
    extract () {
      const n = this.heap.length-1;
      [this.heap[1], this.heap[n]] = [this.heap[n], this.heap[1]];
      let min = this.heap[n];
      this.heap.pop();
      this.traverse();
      console.log( this.heap);
      return min;
    }
  
    extractSlice () {
      let temp = [null]
      let min = this.heap[1];
      this.heap = temp.concat(this.heap.slice(2, this.heap.length));
      this.traverse();
      console.log(this.heap)
      return min;
    }
  
  
  }
  
  let h1 = new MinHeap();
  
  h1.insert(10).insert(5).insert(2);
  
  console.log(h1.heap);
  console.log(h1.extract());
  
  let h2 = new MinHeap();
  
  h2.insert(6).insert(8).insert(1);
  
  console.log(h2.heap);
  console.log(h2.extractSlice());
  