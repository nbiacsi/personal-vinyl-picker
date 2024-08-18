import csv


def format(row: list[str]) -> str:
    """
    Seperates the album name and artist name with a hyphen.

    Args:
        row (list[str]): Row that has an album name and an artist name.

    Returns:
        str: Album Name - Artist Name
    """
    return f"{row[0]} - {row[1]}"


def before(
    index: int,
    *,
    sorted_sheet: list[str],
    wall_album_list: list[str],
    sorted_sheet_count: int,
) -> list[str] | None:
    """
    Gets the album that comes before the one that is picked on the rack.

    Args:
        index (int): Randomly generated number.
        sorted_sheet (list[str]): Sorted CSV sheet of albums. First column is album name, second is artist name.
        wall_album_sheet (list[str]): CSV sheet of albums on the wall. Same formatting as sorted_sheet.
        sorted_sheet_count (int): Count of albums in the sorted sheet of all albums.

    Returns: Album | None
    """
    if index == 0:
        return

    try:
        before = sorted_sheet[index - 1]
    except IndexError:
        return
    
    if before not in wall_album_list:
        return before

    for i in range(2, sorted_sheet_count):
        current_album = sorted_sheet[index - i]
        if current_album in wall_album_list:
            continue

        return current_album


def after(
    index: int,
    *,
    sorted_sheet: list[str],
    wall_album_list: list[str],
    sorted_sheet_count: int,
) -> list[str] | None:
    """
    Gets the album that comes after the one that is picked on the rack.

    Args:
        index (int): Randomly generated number.
        sorted_sheet (list[str]): Sorted CSV sheet of albums. First column is album name, second is artist name.
        wall_album_sheet (list[str]): CSV sheet of albums on the wall. Same formatting as sorted_sheet.
        sorted_sheet_count (int): Count of albums in the sorted sheet of all albums.

    Returns: Album | None
    """
    if index > sorted_sheet_count + 1:
        return

    try:
        after = sorted_sheet[index + 1]
    except IndexError:
        return
    
    if after not in wall_album_list:
        return after

    for i in range(2, sorted_sheet_count):
        current_album = sorted_sheet[index + i]
        if current_album in wall_album_list:
            continue

        return current_album


def get_sorted_albums(sheet: str) -> list[str]:
    """
    Opens a CSV sheet of albums and sorts them by artist and then by album name.

    Args:
        sheet (str): The file path of the CSV sheet.

    Returns:
        Sorted list of albums
    """
    with open(sheet, "r") as albums:
        reader = csv.reader(albums)
        next(reader)
        return sorted(reader, key=lambda row: (row[1], row[0]))


def get_wall_albums(sheet: str) -> list[str]:
    """
    Opens a CSV sheet of albums on the wall.

    Args:
        sheet (str): The file path of the sheet.

    Returns:
        List of albums on the wall.
    """
    with open(sheet, "r") as wallAlbums:
        reader = csv.reader(wallAlbums)
        next(reader)
        return sorted(reader, key=lambda row: (row[1], row[0]))
