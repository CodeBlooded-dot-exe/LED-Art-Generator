from PIL import Image, ImageDraw  # pip install pillow

# 1. Grid and pixel size
cols, rows = 32, 16          # or larger, e.g. 32x32, to fit both
pixel_size = 20

# 2. Colors (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Mario-ish
M_RED = (247, 57, 16)    # hat/shirt [web:29]
M_DARK_RED = (174, 57, 30)    # outline/shadow [web:29]
M_SKIN = (255, 203, 164)  # skin tone [web:29]
M_BROWN = (174, 57, 30)    # hair/boots [web:29]
M_BLUE = (14, 118, 176)   # overalls [web:29]

# Peach-ish
P_SKIN = (245, 226, 184)  # face/arms [web:38]
P_PINK = (246, 177, 208)  # dress light [web:30]
P_PINK_D = (246, 98, 153)   # dress dark [web:38]
P_HAIR = (253, 223, 141)  # hair [web:38]
P_GEM_BLUE = (14, 118, 176)   # jewel [web:28]

# Start with all black pixels
grid = [[BLACK for _ in range(cols)] for _ in range(rows)]

# Example mini-Mario (8x8) at (row 2..9, col 2..9)
mario_pattern = [

    "..RRRRR..",
    ".RRRRRRRRR.",
    ".BBBSS.S..",
    ".BBBBB..",
    ".BMMMB..",
    "..BMB...",
    "..B.B...",
]

char_map = {
    ".": BLACK,
    "R": M_RED,
    "S": M_SKIN,
    "B": M_BLUE,
    "M": M_BROWN,
}

start_row, start_col = 2, 2
for r, row_str in enumerate(mario_pattern):
    for c, ch in enumerate(row_str):
        grid[start_row + r][start_col + c] = char_map[ch]

# Example mini-Peach (8x8) at (row 2..9, col 22..29)
peach_pattern = [
    "........",
    "..HHHH..",
    ".HSSSH..",
    ".SPPPS..",
    ".SPPPS..",
    ".SPPPS..",
    "..P.P...",
    "..P.P...",
]

peach_map = {
    ".": BLACK,
    "H": P_HAIR,
    "S": P_SKIN,
    "P": P_PINK,
}

start_row, start_col = 2, 22
for r, row_str in enumerate(peach_pattern):
    for c, ch in enumerate(row_str):
        grid[start_row + r][start_col + c] = peach_map[ch]

width = cols * pixel_size
height = rows * pixel_size
img = Image.new("RGB", (width, height), BLACK)
draw = ImageDraw.Draw(img)

for y in range(rows):
    for x in range(cols):
        color = grid[y][x]
        x0 = x * pixel_size
        y0 = y * pixel_size
        x1 = x0 + pixel_size
        y1 = y0 + pixel_size
        draw.rectangle([x0, y0, x1, y1], fill=color)

img.save("mario_peach.png")
print("Saved mario_peach.png")
