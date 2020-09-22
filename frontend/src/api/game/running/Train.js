function Train(sketch,train,width,height,scroll) {

  
        this.r = 120;
        this.x = width;
        this.y = height - this.r;
      
      
      this.move = function(){
        this.x -= scroll;
      }
    
      this.show = function() {
        sketch.fill(255,127);
        //rect(this.x, this.y, this.r, this.r)
        sketch.image(train,this.x, this.y, this.r, this.r)
      }
}

export {Train};