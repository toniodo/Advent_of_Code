"""This is day 16 of advent of code 2023"""
from utils.file import list_lines

with open(file="inputs/day_16.txt", mode='r', encoding="utf-8") as f:
    all_lines = list_lines(f)

class Beam:
    """Aclass to describe a beam"""

    def __init__(self, init_pos, init_dir) -> None:
        self.pos = init_pos
        self.dir = init_dir

    def is_out(self) -> bool:
        """Return if the Beam is out out of the tiles"""
        x, y = self.pos
        return x < 0 or x >= n_rows or y < 0 or y >= n_cols

    def do_step(self):
        """ Proceed a step on a beam,
        return a set of beam and a bool to know if the beam is outside"""
        x, y = self.pos
        dx, dy = self.dir
        new_x, new_y = x + dx, y + dy
        if new_x <= -1 or new_x >= n_rows or new_y <= -1 or new_y >= n_cols:
            # Outside the limits
            return None
        if tiles[new_x][new_y] == "\\":
            # Rotation of 90 degrees
            dx, dy = dy, dx
        elif tiles[new_x][new_y] == "/":
            dx, dy = -dy, -dx
        elif tiles[new_x][new_y] == "|" and abs(dy) == 1:
            dx, dy = dy, dx
            # New beams in opposite direction
            return {Beam((new_x, new_y), (dx, dy)), Beam((new_x, new_y), (-dx, -dy))}
        elif tiles[new_x][new_y] == "-" and abs(dx) == 1:
            dx, dy = -dy, -dx
            return {Beam((new_x, new_y), (dx, dy)), Beam((new_x, new_y), (-dx, -dy))}
        # Return a new beam
        return {Beam((new_x, new_y), (dx, dy))}

    def __eq__(self, other) -> bool:
        return self.pos == other.pos and self.dir == other.dir

    def __hash__(self) -> int:
        return hash((self.pos, self.dir))



def throw_beam(init_beam: Beam):
    """Generates beams from an initial beam"""
    # Set of all visited tiles
    tile_visited = set()
    # Set of all beams that are currently spreading on tiles
    current_beams: set[Beam] = set()
    current_beams.add(init_beam)
    # Set of created beam to avoid cycles
    used_beam = set()
    used_beam.add(init_beam)

    while len(current_beams) != 0:
        new_beams: set[Beam] = set()
        removed_beams: set[Beam] = set()
        for beam in current_beams:
            outside = beam.is_out()
            if not outside:
                tile_visited.add(beam.pos)
            if not outside or beam == init_beam:
                out_beams: None | set[Beam] = None
                out_beams = beam.do_step()
                if out_beams is not None:
                    # Add only real new beams
                    new_beams = new_beams.union(out_beams.difference(used_beam))
                    used_beam = used_beam.union(out_beams)
                # Remove current beam
                removed_beams.add(beam)
            else:
                removed_beams.add(beam)

        # Add new beams and remove out beams
        current_beams = current_beams.union(new_beams)
        current_beams.difference_update(removed_beams)
    return len(tile_visited)

tiles = list(map(lambda x: [*x], all_lines))
n_rows = len(tiles)
n_cols = len(tiles[0])

def part_1():
    """Print the solution of part 1"""
    # Initial beam, top corner left going right
    initial_beam = Beam((0, -1), (0, 1))
    number_visit = throw_beam(initial_beam)
    print(f"The total number of visited tiles is {number_visit}")

def part_2():
    """Print the solution of part 2"""
    initial_beams = set()
    for x in range(0, n_rows):
        initial_beams.add(Beam((x,-1),(0,1)))
        initial_beams.add(Beam((x,n_cols),(0,-1)))

    for y in range(0, n_cols):
        initial_beams.add(Beam((-1,y),(1,0)))
        initial_beams.add(Beam((n_rows,y),(-1,0)))


    # Compute the maximum value according to the previous function
    maximum_value = max(map(throw_beam,initial_beams))
    print(f"The maximum value of all initial beam is {maximum_value}")



#Run part 1
part_1()

#Run part 2
part_2()
