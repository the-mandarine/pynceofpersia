from scenery.base import Empty, Floor, Wall

TILES = {\
  '.': [Empty],
  '_': [Floor],
  '#': [Wall],
}

def get_txt_stage():
    stage = """\
###__...
##_._...
##____#.
"""
    return stage

def txt2stage(txt):
    stage = []
    map_y = 0
    for line in txt.split():
        stage.append([])
        map_x = 0
        prev = None
        for tile_chr in line:
            tile_objs = TILES.get(tile_chr, [])
            objs = [obj() for obj in tile_objs]
            if objs and prev is not None:
                objs[0].prev_tile = prev[0]
            stage[map_y].append(objs)
            prev = stage[map_y][-1]
            map_x += 1
        # Link the last tile to the first
        stage[map_y][0][0].prev_tile = stage[map_y][-1][0]
        map_y += 1

    return stage

def get_stage_part(stage, start_x, start_y, max_x=10, max_y=3):
    max_x = min([len(line) for line in stage] + [max_x])
    max_y = min((len(stage), max_y))
    stage_part = [max_x * [None] for i in range(max_y)]
    y = 0
    for line in stage[start_y:start_y+max_y]:
        x = 0
        for tile in line[start_x:start_x+max_x]:
            stage_part[y][x] = tile
            x += 1
        y += 1

    return stage_part
