function Jumper(sketch,height,jumper) {


    this.r = 100;
    this.x = 50;
    this.y = height - this.r;
    this.vy = 0;
    this.gravity = 1.6;


    this.move = function () {
        this.y += this.vy;
        this.vy += this.gravity;

        this.y = sketch.constrain(this.y, 0, height - this.r)
    }

    this.jump = function () {
        if (this.y == height - this.r) {
            this.vy = -31;
            // ding.play();
        }
    }

    this.collide = function (other) {
        let hitX = this.x + this.r - 10 > other.x && this.x < other.x + other.r -40
        let hitY = this.y + this.r -20> other.y
        return (hitX && hitY)
    }

    this.show = function () {
        sketch.fill(255, 127);
        // sketch.rect(this.x, this.y, this.r, this.r)
        sketch.image(jumper,this.x, this.y, this.r, this.r)
    }
}

export {Jumper};