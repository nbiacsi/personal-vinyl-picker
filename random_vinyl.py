"""
    Author: Sloth
    Date: 4/3/2024
    Description: Script to get a random vinyl and get the albums next that are
                    in front and behind it on the rack if not on the wall.
"""

# Built-in imports.
import random

# Custom imports.
from vinyls import format, before, after, get_sorted_albums, get_wall_albums


# Main function of the script.
def main() -> None:
    vinyl_sheet: list[str] = r"C:\Users\nickb\OneDrive\Misc\Scripts\Vinyls\Vinyls.csv"
    wall_vinyl_sheet: list[str] = (
        r"C:\Users\nickb\OneDrive\Misc\Scripts\Vinyls\Wall Vinyls.csv"
    )
    sorted_sheet: list[str] = get_sorted_albums(vinyl_sheet)
    sorted_sheet_count: int = len(sorted_sheet)
    wall_album_list: list[str] = get_wall_albums(wall_vinyl_sheet)

    # Get a random number one less than the amount of albums and grab the album at that index.
    index: int = random.randint(0, (len(sorted_sheet) - 1))
    album: list[str] = sorted_sheet[index]
    print(f"\nYour random album is: {format(album)}\n")

    # If the album is on the wall, nothing further is needed to be done in terms of placing the vinyl in the correct location.
    if album in wall_album_list:
        print("Album is on the wall.\n")
        return

    # Get the albums that come one before and one after the random album, if they exist.
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

    # Print the albums that come one before and one after the random album.
    print(f"Albums that come one before and one after {format(album)}:\n")
    if before_album is None:
        print("No album comes before this album.")
    else:
        print(f"Before: {format(before_album)}")
    if after_album is None:
        print("No album comes after this album.")
    else:
        print(f"After: {format(after_album)}")


if __name__ == "__main__":
    main()
