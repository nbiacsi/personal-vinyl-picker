'''
    Author: Sloth
    Date: 8/24/2025
    Description: Script to get a random vinyl and get the albums next that are in front and behind it on the rack if not on the wall.
'''

import random

from vinyls import format, before, after, get_albums


def main() -> None:
    vinyl_sheet: str = '/mnt/misc/Misc/Scripts/Vinyls/personal-vinyl-picker/Vinyls.csv'
    wall_vinyl_sheet: str = '/mnt/misc/Misc/Scripts/Vinyls/personal-vinyl-picker/Wall Vinyls.csv'
    sorted_sheet: list[list[str]] = get_albums(vinyl_sheet)
    sorted_sheet_count: int = len(sorted_sheet)
    wall_album_list: list[list[str]] = get_albums(wall_vinyl_sheet)

    index: int = random.randint(0, (len(sorted_sheet) - 1))
    album: list[str] = sorted_sheet[index]
    print(f'\nYour random album is: {format(album)}\n')

    if album in wall_album_list:
        print('Album is on the wall.\n')
        return

    before_album = before(
        index,
        sorted_sheet=sorted_sheet,
        wall_album_list=wall_album_list,
        sorted_sheet_count=sorted_sheet_count,
    )
    after_album = after(
        index,
        sorted_sheet=sorted_sheet,
        wall_album_list=wall_album_list,
        sorted_sheet_count=sorted_sheet_count,
    )

    if before_album == None:
        print('No album comes before this album.')
    else:
        print(f'Before: {format(before_album)}')

    if after_album == None:
        print('No album comes after this album.')
    else:
        print(f'After: {format(after_album)}')


if __name__ == '__main__':
    main()
