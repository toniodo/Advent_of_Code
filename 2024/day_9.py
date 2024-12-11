"""Day 9 AoC 2024"""
from dataclasses import dataclass
from utils.parse import simple_parse
from copy import copy

line = simple_parse("inputs/9.txt")[0]
disk_grid = [int(elt) for elt in line]


@dataclass
class FreeSpace:
    size: int
    id: int


@dataclass
class FileBlock:
    size: int
    id: int


def rearrange_disk(disk: list[FreeSpace | FileBlock]):
    """Rearrange a given disk"""
    new_disk = []
    for id_block, block in enumerate(disk):
        if isinstance(block, FreeSpace) and block.size != 0:
            while block.size != 0:
                # We have a FreeSpace
                # Find the last FileBlock
                for ind_r_end, block_end in enumerate(disk[::-1]):
                    if isinstance(block_end, FileBlock) and block_end.size != 0:
                        last_block = block_end
                        ind_end = len(disk) - ind_r_end - 1
                        break

                if ind_end <= id_block:
                    # The disk is already rearranged
                    return new_disk

                # More free space than the file block
                if block.size > last_block.size:
                    new_disk.append(copy(last_block))
                    block.size -= last_block.size
                    last_block.size = 0

                # Less free space than the file block
                elif block.size < last_block.size:
                    sub_block = FileBlock(block.size, last_block.id)
                    new_disk.append(sub_block)
                    last_block.size -= block.size
                    block.size = 0

                else:
                    # Equality of sizes
                    new_disk.append(copy(last_block))
                    block.size = 0
                    last_block.size = 0

        elif block.size != 0:
            new_disk.append(block)

    return new_disk


def compute_check_sum(disk):
    """Compute the checksum for a given disk"""
    current_id = 0
    checksum = 0
    for block in disk:
        for ind in range(current_id, current_id + block.size):
            if isinstance(block,FileBlock):
                checksum += ind * block.id
            current_id += 1
    return checksum

# Part 1
format_disk = []
is_block = True
ind = 0
for space in disk_grid:
    if is_block:
        format_disk.append(FileBlock(space, ind))
        is_block = False
    else:
        format_disk.append(FreeSpace(space, ind))
        is_block = True
        ind += 1

rearranged_disk = rearrange_disk(format_disk)
print("The sum of all checksums is", compute_check_sum(rearranged_disk))


def rearrange_disk_next(disk: list[FreeSpace | FileBlock]):
    """Rearrange a given disk"""
    new_disk = []
    for id_block, block in enumerate(disk):
        if isinstance(block, FreeSpace) and block.size != 0:
            # We have a FreeSpace
            # Find the last FileBlock that fits
            for ind_r_end, block_end in enumerate(disk[::-1]):
                if isinstance(block_end, FileBlock) and block_end.size != 0 and block_end.size <= block.size:
                    last_block = block_end
                    ind_end = len(disk) - ind_r_end - 1

                    # Place the block
                    if ind_end <= id_block:
                        # The disk is already rearranged
                        continue

                    elif block.size == last_block.size:
                        # Equality of sizes
                        new_disk.append(copy(last_block))
                        block.size = 0
                        disk[ind_end] = FreeSpace(last_block.size, 0)

                    # More free space than the file block
                    else:
                        new_disk.append(copy(last_block))
                        block.size -= last_block.size
                        disk[ind_end] = FreeSpace(last_block.size, 0)
            if block.size != 0:
                new_disk.append(copy(block))            

        elif block.size != 0:
            new_disk.append(copy(block))

    return new_disk

# Part 2
format_disk = []
is_block = True
ind = 0
for space in disk_grid:
    if is_block:
        format_disk.append(FileBlock(space, ind))
        is_block = False
    else:
        format_disk.append(FreeSpace(space, ind))
        is_block = True
        ind += 1
rearranged_disk_2 = rearrange_disk_next(format_disk)
print("The sum of all checksums is", compute_check_sum(rearranged_disk_2))
