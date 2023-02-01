import math

def ball_collide(ball1, ball2):
    (x1, y1, r1) = ball1
    (x2, y2, r2) = ball2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if distance <= (r1 + r2):
        return True
    else:
        return False

# Example usage:
ball1 = (0, 0, 5)
ball2 = (10, 0, 5)

if ball_collide(ball1, ball2):
    print("The balls are colliding.")
else:
    print("The balls are not colliding.")
