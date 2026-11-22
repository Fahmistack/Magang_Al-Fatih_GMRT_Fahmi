import math

H0 = 0.06       # jarak base_link ke joint_1 (m)
L1 = 0.04       # jarak joint_1 ke joint_2 (m)
L2 = 0.25       # jarak joint_2 ke joint_3 (m)
OFFSET2 = 0.6   # sudut awal joint_2 di URDF (rad)

JOINT_1 = 0.5
JOINT_2 = 0.10


def joint3_position(q1, q2):
    """q1, q2 dalam radian. Return posisi joint_3 (x, y, z) dalam meter."""
    theta = q2 + OFFSET2              # sudut link 2 dari garis tegak
    r = L2 * math.sin(theta)          # jarak mendatar
    x = r * math.cos(q1)
    y = r * math.sin(q1)
    z = H0 + L1 + L2 * math.cos(theta)
    return x, y, z

if __name__ == "__main__":
    x, y, z = joint3_position(JOINT_1, JOINT_2)
    print(f"Posisi joint_3: X = {x:.5f}  Y = {y:.5f}  Z = {z:.5f} m")