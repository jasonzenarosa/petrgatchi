export class particle {
    constructor(x, y, speed, angle) {
        this._x = x;
        this._y = y;
        this._speed = speed;
        this._angle = angle;
    }

    get_position() {
        return [this._x, this._y];
    }

    set_location(x, y) {
        this._x = x;
        this._y = y;
    }

    change_location(dx, dy) {
        this._x += dx;
        this._y += dy;
    }

    get_angle() {
        return this._angle;
    }

    set_angle(angle) {
        this._angle = angle;
    }

    get_speed() {
        return this._speed;
    }

    set_speed(speed) {
        this._speed = speed;
    }

    set_velocity(speed, angle) {
        this.set_speed(speed);
        this.set_angle(angle);
    }

    randomize_angle() {
        this.set_angle(2*Math.PI*Math.random())
    }

    move() {
        this.change_location(this.get_speed()*Math.cos(this.get_angle()), this.get_speed()*Math.sin(this.get_angle()))
    }
}