from scenery.base import *
from pydoc import locate
import os
import json

BASE_STAGE_PATH = "stages"

TILES = {\
  '.': [Empty],
  'i': [EmptyTorch],
  '_': [Floor],
  'I': [FloorTorch],
  '#': [Wall],
  '@': [Stairs],
}

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
    max_x, max_y = (0, 0)

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
            for tile_chr in line:
                tile_objs = TILES.get(tile_chr, [DEFAULT_TILE()])
                objs = [obj() for obj in tile_objs]
                self.stage[map_y].append(objs)
                map_x += 1
                self.max_x = max(self.max_x, map_x)

            map_y += 1
        self.max_y = map_y

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

    def get_scr_pos(self, res_x, res_y, tps_x=10, tps_y=4):
        screen_y = max(0, int(res_y / tps_y) * tps_y - 1)
        scr_x = res_x % tps_x
        scr_y = res_y - screen_y
        return scr_x, scr_y

    def get_screen(self, hero_x, hero_y, tps_x=10, tps_y=4, scrolling=False):
        scr_x = int(hero_x / tps_x) * tps_x
        scr_y = max(0, int(hero_y / tps_y) * tps_y - 1)
        max_scr_x = tps_x
        max_scr_y = min(len(self.stage) - scr_y, tps_y)
        part = [max_scr_x * [[Empty()]] for i in range(max_scr_y)]

        y = 0
        for line in self.stage[scr_y:scr_y+max_scr_y]:
            x = 0
            for tile in line[scr_x:scr_x+max_scr_x]:
                part[y][x] = tile
                for element in tile:
                    element.screen_pos = (x, y-1)
                x += 1
            y += 1

        # if not enough lines, add some


        return part
