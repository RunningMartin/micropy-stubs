# make_stub_files: Wed 04 Sep 2019 at 21:10:42

from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class Motor:
    def __init__(self, port: Port, direction: Direction=Direction.CLOCKWISE, gears: List[(int, int)]=None) -> None: ...
    def dc(self, duty: float) -> None: ...
    def angle(self) -> None: ...
    def reset_angle(self, angle: int) -> None: ...
    def speed(self) -> None: ...
    def stop(self, stop_type: Stop=Stop.COAST) -> None: ...
    def run(self, speed: int) -> None: ...
    def run_time(self, speed: int, time: int, stop_type: Stop=Stop.COAST, wait: bool=bool) -> None: ...
    def run_angle(self, speed: int, rotation_angle: int, stop_type: Stop=Stop.COAST, wait: bool=bool) -> None: ...
    def run_target(self, speed: int, target_angle: int, stop_type: Stop=Stop.COAST, wait: bool=bool) -> None: ...
    def track_target(self, target_angle: int) -> None: ...
    def stalled(self) -> None: ...
    def run_until_stalled(self, speed: int, stop_type: Stop=Stop.COAST, duty_limit: float=100) -> None: ...
    def set_dc_settings(self, duty_limit: float=100, duty_offset: float=0.0) -> None: ...
    def set_run_settings(self, max_speed: int, acceleration: int) -> None: ...
    def set_pid_settings(self, kp: int, ki: int, kd: int, tight_loop_limit: float, angle_tolerance: int, speed_tolerance: int, stall_speed: int, stall_time: int) -> None: ...
class TouchSensor:
    def __init__(self, port: Port) -> None: ...
    def pressed(self) -> None: ...
class ColorSensor:
    def __init__(self, port: Port) -> None: ...
    def color(self) -> None: ...
    def ambient(self) -> None: ...
    def reflection(self) -> None: ...
    def rgb(self) -> None: ...
class InfraredSensor:
    def __init__(self, port: Port) -> None: ...
    def distance(self) -> None: ...
    def beacon(self, channel: int) -> None: ...
    def buttons(self, channel: int) -> None: ...
class UltrasonicSensor:
    def __init__(self, port: Port) -> None: ...
    def distance(self, silent: bool=bool) -> None: ...
    def presence(self) -> None: ...
class GyroSensor:
    def __init__(self, port: Port, direction: Direction=Direction.CLOCKWISE) -> None: ...
    def speed(self) -> None: ...
    def angle(self) -> None: ...
    def reset_angle(self, angle: int) -> None: ...