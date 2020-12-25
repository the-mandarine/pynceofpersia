from scenery.base import Empty, Stairs, Floor, Wall
from pydoc import locate
import os
import json

BASE_STAGE_PATH = "stages"

TILES = {\
  '.': [Empty],
  '_': [Floor],
  '#': [Wall],
  '@': [Stairs],
}

STAGE_START = '@'

DEFAULT_TILE = Empty

class Pos(list):
    def __init__(self, y, x):
        super().__init__((int(y), int(x),))

def parse_resource(resource):
    res_type_s, res_args_s = resource.split(':')
    res_args = res_args_s.split(',')
    #

    res_type = locate(res_type_s)
    resource = res_type(*res_args)

    return resource

def parse_stage(path):
    spath = os.path.join(BASE_STAGE_PATH, path)
    resources = {}
    map = ""
    map_started = False
    with open(spath, 'r') as sfile:
        for line in sfile:
            if map_started:
                map += line
            elif not line.strip():
                map_started = True
                continue
            else:
                # parse resource
                key, value = line.split(":", 1)
                resources[key] = parse_resource(value.strip())

    print("Stage map:")
    print(map)
    return map, resources


class Stage(object):
    start_pos = (0, 0)

    def __init__(self, stage_path=""):
        self.stage_path = stage_path
        self.txtmap, self.resources = parse_stage(stage_path)

        self.build_stage()
        self.add_resources()

    def build_stage(self):
        self.stage = []
        map_y = 0
        for line in self.txtmap.split():
            if not line:
                continue
            self.stage.append([])
            map_x = 0
            left = None
            for tile_chr in line:
                tile_objs = TILES.get(tile_chr, [DEFAULT_TILE()])
                objs = [obj() for obj in tile_objs]
                self.stage[map_y].append(objs)
                if tile_chr == STAGE_START:
                    self.start_pos = (map_x, map_y)
                map_x += 1

            map_y += 1

        # Link all tiles together and add positions
        map_y = 0
        for line in self.stage:
            map_x = 0
            for tile in line:
                if map_y == 0:
                    tile[0].top = None
                else:
                    tile[0].top = self.stage[map_y-1][map_x][0]

                if map_y + 1 == len(self.stage):
                    tile[0].bottom = None
                else:
                    tile[0].bottom = self.stage[map_y+1][map_x][0]

                # looping left/right
                tile[0].left = line[map_x-1][0]
                line[map_x-1][0].right = tile[0]

                tile[0].map_pos = (map_x, map_y)
                map_x += 1
            map_y += 1

    def add_resources(self):
        for res_key, res_value in self.resources.items():
            print(res_key, ':', repr(res_value))
            super().__setattr__(res_key, res_value)

    def get_stage_part(self, start_x, start_y, max_x=10, max_y=3, scrolling=False):
        max_x = min([len(line) for line in self.stage] + [max_x])
        max_y = min((len(self.stage), max_y)) + 1
        stage_part = [max_x * [None] for i in range(max_y)]
        if start_y == 0:
            # add empty top-line if we request it
            stage_part[0] = [[DEFAULT_TILE()] for i in range(max_x)]
            screen_x = 0
            for tile in stage_part[0]:
                for element in tile:
                    element.screen_pos = (screen_x, -1)
                screen_x += 1

        y = 0
        for line in self.stage[start_y:start_y+max_y]:
            x = 0
            for tile in line[start_x:start_x+max_x]:
                stage_part[y][x] = tile
                for element in tile:
                    element.screen_pos = (x, y-1)
                x += 1
            y += 1

        return stage_part
