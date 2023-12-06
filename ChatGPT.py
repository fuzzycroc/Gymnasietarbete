import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Body:
    def __init__(self, mass, x, y, vx, vy):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy


def update_position(body, dt):
    body.x += body.vx * dt
    body.y += body.vy * dt

def update_velocity(body, ax, ay, dt):
    body.vx += ax * dt
    body.vy += ay * dt

def update(frame):
    global body1, body2

    G = 1
    r_squared = (body1.x - body2.x)**2 + (body1.y - body2.y)**2
    force = G * body1.mass * body2.mass / r_squared

    ax = -force * (body1.x - body2.x) / (r_squared**0.5 * body1.mass)
    ay = -force * (body1.y - body2.y) / (r_squared**0.5 * body1.mass)

    update_velocity(body1, ax, ay, dt)
    update_position(body1, dt)

    update_velocity(body2, -ax, -ay, dt)
    update_position(body2, dt)

    line.set_data([body1.x, body2.x], [body1.y, body2.y])
    scat.set_offsets([(body1.x, body1.y), (body2.x, body2.y)])

fig, ax = plt.subplots()
line, = ax.plot([], [], 'r-')
scat = ax.scatter([], [], c=['red', 'blue'], marker='o')

ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

body1 = Body(mass=1, x=0, y=0, vx=12, vy=1)
body2 = Body(mass=1, x=1, y=1, vx=2, vy=1)

dt = 0.01

animation = FuncAnimation(fig, update, frames=range(100), interval=50)
plt.show()
