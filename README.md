# arm_model

Model URDF robot arm 3 DOF sederhana untuk ROS 2 Jazzy, lengkap dengan launch file untuk menampilkannya di RViz.

## Struktur Robot

Arm terdiri dari 4 link dan 3 joint:

```
base_link (link_1) -> joint_1 -> link_2 -> joint_2 -> link_3 -> joint_3 -> link_4 (gripper)
```

| Joint | Menghubungkan | Sumbu putar | Fungsi |
|---|---|---|---|
| `joint_1` | `base_link` -> `link_2` | Z | Yaw (putar badan) |
| `joint_2` | `link_2` -> `link_3` | Y | Bahu |
| `joint_3` | `link_3` -> `link_4` | Y | Siku, langsung terhubung ke gripper |

Semua joint bertipe `revolute` dengan limit ±1.57 rad. Pose awal (joint = 0) sengaja dibuat membungkuk lewat sudut `rpy` di origin `joint_2` dan `joint_3`.

## Warna Bagian

| Bagian | Warna |
|---|---|
| Alas | abu gelap |
| Kolom | abu terang (steel) |
| Turret | biru |
| Sendi bahu | cyan |
| Lengan atas | oranye |
| Sendi siku | kuning |
| Lengan bawah | hijau |
| Telapak gripper | ungu |
| Jari gripper | merah |

## Struktur Package

```
arm_model/
├── config/rviz_config.rviz   # konfigurasi RViz
├── launch/display.launch.py  # launch robot_state_publisher, joint_state_publisher_gui, RViz
├── urdf/arm.urdf             # model robot
├── package.xml
└── setup.py
```

## Kebutuhan

- Ubuntu dengan ROS 2 Jazzy
- Paket berikut:

```bash
sudo apt update
sudo apt install ros-jazzy-robot-state-publisher ros-jazzy-joint-state-publisher-gui ros-jazzy-xacro
```

## Cara Pakai

Taruh package di folder `src/` workspace, lalu dari folder workspace:

```bash
source /opt/ros/jazzy/setup.bash
colcon build --packages-select arm_model --symlink-install
source install/setup.bash
ros2 launch arm_model display.launch.py
```

RViz akan terbuka bersama jendela slider. Geser slider `joint_1`, `joint_2`, dan `joint_3` untuk menggerakkan arm.

Dengan `--symlink-install`, perubahan pada URDF, launch file, atau config RViz langsung terbaca saat launch dijalankan ulang, tanpa build ulang.
