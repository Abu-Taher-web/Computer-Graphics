import glm
import math


class MVPController:
    def __init__(self, callback_update, width: int, height: int):
        self.callback_update = callback_update
        self.width = width
        self.height = height
        self.position = glm.vec3(2, 2, 2.5)
        target = glm.vec3(0, 0, 0)
        direction_to_target = glm.normalize(target - self.position)
        self.pitch = math.asin(direction_to_target.y)
        self.yaw = math.atan2(direction_to_target.z, direction_to_target.x)
        self.roll = 0.0
        self.speed = 0.4
        self.mouse_speed = 0.01
        self.fov = 90
        self.calc_view_projection()
        self.last_x = 0
        self.last_y = 0

    def calc_mvp(self, model_matrix=glm.mat4(1.0)):
        return self.projection_matrix * self.view_matrix * model_matrix

    def calc_view_projection(self):
        self.direction = glm.vec3(
            math.cos(self.yaw) * math.cos(self.pitch),
            math.sin(self.pitch),
            math.sin(self.yaw) * math.cos(self.pitch)
        )
        world_up = glm.vec3(0, -1, 0)
        self.right = glm.normalize(glm.cross(world_up, self.direction))
        self.up = glm.normalize(glm.cross(self.right, self.direction))
        self.view_matrix = glm.lookAt(self.position,
                          self.position + self.direction,
                          self.up)

        self.projection_matrix = glm.perspective(glm.radians(self.fov), self.width / self.height, 0.1, 1000)

    def on_keyboard(self, key: bytes, x: int, y: int):
        if key == b'w':  # Move forward
            self.position += self.direction * self.speed
        elif key == b's':  # Move backward
            self.position -= self.direction * self.speed
        elif key == b'a':  # Move left
            self.position += self.right * self.speed
        elif key == b'd':  # Move right
            self.position -= self.right * self.speed
        elif key == b'e':  # Move up
            self.position += self.up * self.speed
        elif key == b'r':  # Move down
            self.position -= self.up * self.speed    
        self.calc_view_projection()
        self.callback_update()

    def on_mouse(self, key: int, up: int, x: int, y: int):
        if key == 0:  # Left button
            self.is_dragging = (up == 0)  # Press if up is 0
        if self.is_dragging:
            self.last_x = x
            self.last_y = y

    def on_mousemove(self, x: int, y: int):
        x_diff = self.last_x - x
        y_diff = y - self.last_y
        self.last_x = x
        self.last_y = y
        self.yaw += x_diff * self.mouse_speed
        self.pitch += y_diff* self.mouse_speed
        self.pitch = max(-math.pi/2, min(math.pi/2, self.pitch))
        self.calc_view_projection()
        self.callback_update()

    def on_special_key(self, *args):
        pass

