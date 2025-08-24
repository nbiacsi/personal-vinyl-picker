'''
    Author: Sloth
    Date: 8/24/2025
    Description: Vinyl module for utility functions for Vinyls.
'''

import csv


def format(row: list[str]) -> str:
    '''
    Seperates the album name and artist name with a hyphen.

    Args:
        row (list[str]): Row that has an album name and an artist name.

    Returns:
        str: Album Name - Artist Name
    '''
    return f'{row[0]} - {row[1]}'


def before(
    index: int,
    *,
    sorted_sheet: list[list[str]],
    wall_album_list: list[list[str]],
    sorted_sheet_count: int,
) -> list[str] | None:
    '''
    Gets the album that comes before the one that is picked on the rack.

    Args:
        index (int): Randomly generated number.
        sorted_sheet (list[str]): Sorted CSV sheet of albums. First column is album name, second is artist name.
        wall_album_sheet (list[str]): CSV sheet of albums on the wall. Same formatting as sorted_sheet.
        sorted_sheet_count (int): Count of albums in the sorted sheet of all albums.

    Returns: Album | None
    '''

    if index == 0:
        return

    before: list[str] = sorted_sheet[index - 1]
    if before not in wall_album_list:
        return before

    for i in range(2, sorted_sheet_count):
        current_album: list[str] = sorted_sheet[index - i]
        if current_album not in wall_album_list:
            return current_album


def after(
    index: int,
    *,
    sorted_sheet: list[list[str]],
    wall_album_list: list[list[str]],
    sorted_sheet_count: int,
) -> list[str] | None:
    '''
    Gets the album that comes after the one that is picked on the rack.

    Args:
        index (int): Randomly generated number.
        sorted_sheet (list[str]): Sorted CSV sheet of albums. First column is album name, second is artist name.
        wall_album_sheet (list[str]): CSV sheet of albums on the wall. Same formatting as sorted_sheet.
        sorted_sheet_count (int): Count of albums in the sorted sheet of all albums.

    Returns: Album | None
    '''

    if index == sorted_sheet_count - 1:
        return

    after: list[str] = sorted_sheet[index + 1]
    if after not in wall_album_list:
        return after

    for i in range(2, sorted_sheet_count):
        current_album = sorted_sheet[index + i]
        if current_album not in wall_album_list:
            return current_album
    

def get_albums(file_path) -> list[list[str]]:
    '''
    Opens a CSV sheet of albums.

    Args:
        sheet (str): The file path of the sheet.

    Returns:
        List of albums.
    '''

    with open(file_path) as albums:
        reader = csv.reader(albums)
        next(reader)
        return sorted(reader, key=lambda row: (row[1], row[0]))
