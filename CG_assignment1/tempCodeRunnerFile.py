angle = time.time() - start_time
		self.model_matrix = glm.rotate(glm.mat4(1), angle, glm.vec3(1, 0, 0))
