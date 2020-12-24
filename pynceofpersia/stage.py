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
        if not line:
            continue
        stage.append([])
        map_x = 0
        left = None
        for tile_chr in line:
            tile_objs = TILES.get(tile_chr, [Empty])
            objs = [obj() for obj in tile_objs]
            stage[map_y].append(objs)
            map_x += 1

        map_y += 1

    # Link all tiles together and add positions
    map_y = 0
    for line in stage:
        map_x = 0
        for tile in line:
            if map_y == 0:
                tile[0].top = None
            else:
                tile[0].top = stage[map_y-1][map_x][0]

            if map_y + 1 == len(stage):
                tile[0].bottom = None
            else:
                tile[0].bottom = stage[map_y+1][map_x][0]

            # looping left/right
            tile[0].left = line[map_x-1][0]
            line[map_x-1][0].right = tile[0]

            tile[0].map_pos = (map_x, map_y)
            map_x += 1
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