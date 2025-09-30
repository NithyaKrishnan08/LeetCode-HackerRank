# Google Document Parser

import requests
import re

def print_google_doc_grid(doc_url: str):
    """
    Fetches a published Google Doc (as plain text), parses coordinates and characters,
    and prints the 2D grid of characters (the secret message).
    """

    # Ensure the URL ends with /pub (published link)
    if "/edit" in doc_url:
        doc_url = doc_url.split("/edit")[0] + "/pub"

    response = requests.get(doc_url)
    response.raise_for_status()
    text = response.text

    # Regex for lines like: "Character: █  X: 2  Y: 3"
    pattern = re.compile(r"Character:\s*(.)\s*X:\s*(\d+)\s*Y:\s*(\d+)")
    matches = pattern.findall(text)

    if not matches:
        print("No character data found in document.")
        return

    # Map positions to characters
    grid = {}
    max_x, max_y = 0, 0
    for char, x, y in matches:
        x, y = int(x), int(y)
        grid[(x, y)] = char
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    # Build and print grid
    for y in range(max_y + 1):
        row = []
        for x in range(max_x + 1):
            row.append(grid.get((x, y), " "))
        print("".join(row))

if __name__ == "__main__":
    url = "https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub"
    print_google_doc_grid(url)