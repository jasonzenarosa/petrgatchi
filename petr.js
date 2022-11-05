export class particle {
    constructor(x, y, mw, mh, speed, angle) {
        this._x = x;
        this._y = y;
        this.mw = mw;
        this.mh = mh;
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
        this.set_angle(2*Math.PI*Math.random());
    }

    move() {
        this.change_location(this.get_speed()*Math.cos(this.get_angle()), this.get_speed()*Math.sin(this.get_angle()));
        this.wall_bounce();
    }

    bounce(barrier_angle) {
        this.set_angle(2 * barrier_angle - this.get_angle());
    }

    wall_bounce() {
        let [x, y] = this.get_position();
        let [w, h] = [200, 200];
        let [mw, mh] = [this.mw, this.mh];

        let left_x   = x;
        let right_x  = x + w;
        let top_y    = y;
        let bottom_y = y + h;

        if (left_x < 300) {
            this.bounce(Math.PI / 2);
            // this.change_location(-2*left_x, 0);

        } else if (right_x > mw-300) {
            this.bounce(Math.PI / 2);
            // this.change_location(2*(mw-right_x), 0);
        }
        
        if (bottom_y < 300) {
            this.bounce(0);
            // this.change_location(0, -2*top_y);

        } else if (top_y > mh-300) {
            this.bounce(0);
            // this.change_location(0, 2*(mh-bottom_y));
        }

    }
}