#!/usr/bin/env python3


def pass_through_door(a, b, c, w, h):
    box_dim = [a, b, c]  # box dimensions
    # If the two smaller box sides pass, then whole box is passing through the door
    box_dim.remove(max(box_dim))
    if box_dim[0] <= min(w, h) or box_dim[1] <= min(w, h):
        if box_dim[0] <= max(w, h) and box_dim[1] <= max(w, h):
            return 'box passes'
    return 'box doesn\'t passes'

if __name__ == '__main__':
    print(pass_through_door(1.6, 0.9, 0.60, 0.6, 1.6))
    print(pass_through_door(1.61, 1.7, 0.45, 0.6, 1.6))
