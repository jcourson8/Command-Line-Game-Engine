import copy
import threading
import time


class Object():
    def __init__(self, relative_location_mapping, origin_location, physics_on=False, velocity=(0, 0)):
        # map_dict defined as dict, with locations relative to (0,0) for certain symbols as keys)
        # key must be single char
        # {'symb':[(),()],'symb2'
        self.relative_location_mapping = copy.deepcopy(
            relative_location_mapping)
        self.origin_location = origin_location
        self.boundary = self._calculate_boundary_box()
        self.rendering_map = self._calculate_rendering_map(
            self.relative_location_mapping, self.origin_location)
        self.time = time.time()

        self.physics_on = physics_on
        if self.physics_on == True:
            self.turn_physics_on(velocity)

    def _calculate_boundary_box(self):
        # returns largest x,y in relative location
        # self.get_origin_location()

        # loop through r_l_m keys for each key find the smallest x,y and largest x,y
        # this is kinda a crusty way to do this, but the though was it would be
        # better to sort it oncerather than finding the max and min twice for the x's and the y's
        x_list = []
        y_list = []
        for value_list in self.relative_location_mapping.values():
            value_list_sorted_by_x = sorted(
                value_list, key=lambda cord: cord[0])
            x_list.append(value_list_sorted_by_x[0][0])
            x_list.append(value_list_sorted_by_x[-1][0])
            value_list_sorted_by_y = sorted(
                value_list, key=lambda cord: cord[1])
            y_list.append(value_list_sorted_by_y[0][1])
            y_list.append(value_list_sorted_by_y[-1][1])

        x_pos = max(x_list)
        x_neg = min(x_list)
        y_pos = max(y_list)
        y_neg = min(y_list)

        return (x_pos, x_neg, y_pos, y_neg)

    def get_boundary(self):
        return self.boundary

    def get_origin_location(self):
        return self.origin_location

    def update_origin_location(self, origin_location):
        # helpful check not to do extra work if we don't have to
        if origin_location == self.origin_location:
            return
        x = origin_location[0] - self.origin_location[0]
        y = origin_location[1] - self.origin_location[1]
        origin_difference = (x, y)
        new_origin = (self.origin_location[0]+x, self.origin_location[1]+y)

        self.origin_location = new_origin

        self.rendering_map = self._calculate_rendering_map(
            self.rendering_map, origin_difference)

        self.time_last_updated = time.time()

    def _calculate_rendering_map(self, rendering_map, origin_difference):
        if origin_difference == (0, 0):
            return rendering_map
        new_rendering_map = {}
        # for each key go through its values list and add the difference to each of them
        for i, (key, value_list) in enumerate(rendering_map.items()):
            new_rendering_map[key] = []
            for j, values in enumerate(value_list):
                new_rendering_map[key].append(
                    (values[0]+origin_difference[0], values[1]+origin_difference[1]))
        return new_rendering_map

    def get_rendering_map(self):
        # take the relative_location_map and add the origin location to each of the
        return [tup for tup in self.rendering_map.items()]

    def get_velocity(self):
        return self.velocity

    def update_velocity(self, velocity):  # vel is (x, y)
        if self.physics_on:
            self.velocity = velocity
        else:
            self.turn_physics_on(velocity)

    def _update_location_for_velocity(self):
        while True:
            if self.velocity == (0, 0):
                continue
            cur_time = time.time()
            time_diff = cur_time - self.time_last_updated
            while time_diff < .01:
                cur_time = time.time()
                time_diff = cur_time - self.time_last_updated
                continue
            # self.h = 1
            x, y = self.get_origin_location()
            vx, vy = self.velocity
            # we are defining this as exactly one centisecond has passed
            x, y = x+vx, y+vy
            self.update_origin_location((x, y))

    def turn_physics_on(self, velocity):
        # Physics
        # define it as .01 because vel is defined char/centisecond so it will be updated right away
        # self.time_last_updated = .01 # not working
        self.time_last_updated = time.time()
        self.velocity = velocity  # vx and vy vel. (char/centisecond)
        self.velocity_thread = threading.Thread(
            target=self._update_location_for_velocity)
        self.velocity_thread.start()

    # def _stop_physics_thread(self):
    #     if self.physics_on:
    #         self.velocity_thread.
