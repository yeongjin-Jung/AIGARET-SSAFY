function Jumper (sketch, height, jumper) {
  this.r = 200
  this.x = 50
  this.y = height - this.r
  this.vy = 0
  this.gravity = 1.3

  this.move = function () {
    this.y += this.vy
    this.vy += this.gravity

    this.y = sketch.constrain(this.y, 0, height - this.r)
  }

  this.jump = function () {
    if (this.y == height - this.r) {
      this.vy = -37
      // ding.play();
    }
  }

  this.collide = function (other) {
    const hitX = this.x + this.r - 30 > other.x && this.x < other.x + other.r - 50
    const hitY = this.y + this.r - 50 > other.y
    return (hitX && hitY)
  }

  this.show = function () {
    sketch.fill(255, 127)
    // sketch.rect(this.x, this.y, this.r, this.r)
    sketch.image(jumper, this.x, this.y, this.r, this.r)
  }
}

export { Jumper }
