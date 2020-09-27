
function Snake (sketch, scl, width, height, food) {
  this.x = 0
  this.y = 0
  this.xspeed = 1
  this.yspeed = 0
  this.total = 0
  this.tail = []

  this.eat = function (food) {
    var d = sketch.dist(this.x, this.y, 20 * food.x, 20 * food.y)
    if (d < 1) {
      this.total++
      return true
    } else { return false }
  }

  this.dir = function (x, y) {
    this.xspeed = x
    this.yspeed = y
  }

  this.update = function () {
    if (this.total === this.tail.length) {
      for (var i = 0; i < this.tail.length - 1; i++) {
        this.tail[i] = this.tail[i + 1]
      }
    }

    this.tail[this.total - 1] = sketch.createVector(this.x, this.y)

    this.x = this.x + this.xspeed * scl
    this.y = this.y + this.yspeed * scl

    this.x = sketch.constrain(this.x, 0, width - scl)
    this.y = sketch.constrain(this.y, 0, height - scl)
  }

  this.show = function () {
    sketch.fill(255)
    for (var i = 0; i < this.tail.length; i++) {
      sketch.rect(this.tail[i].x, this.tail[i].y, scl, scl)
    }
    sketch.fill(255)
    sketch.rect(this.x, this.y, scl, scl)
  }
}

export { Snake }
