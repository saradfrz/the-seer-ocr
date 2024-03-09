import pandas as pd
import numpy as np
import os

def generate_list_pattern(length):
    pattern = []
    limit = int(np.floor(length/2))
    for i in range(1, limit + 1):
        pattern.append(f'{i}. White')
        pattern.append(f'{i}. Black')
    if length % 2 == 1:
        pattern.append(f'{limit + 1}. White')
    return pattern

def convert_txt_to_tsv(filename):

    with open(f"output/{filename}", "r", encoding="utf-8") as f:
        text = f.read()

    content = text.split("\n")
    variation = content[0]
    opening = content[1]
    moves = content[3:]

    who_moves = generate_list_pattern(len(moves))

    front = [f"{variation}&nsbp{opening}:&nsbp&nsbp{who_moves[x]}" for x in range(len(who_moves))]

    deck = pd.DataFrame()
    deck["front"] = front
    deck["back"] = moves

    filename = f"{variation}_{opening}".lower().replace('..','_').replace(' ','_').replace('-','_')
    deck.to_csv(f"decks/{filename}.tsv", sep='\t', header=False, index=False)


def get_filenames():
    filenames = []

    for filename in os.listdir("output"):
        if os.path.isfile(os.path.join("output", filename)):
            filenames.append(filename)
    return filenames


if __name__ == "__main__":
    filenames = get_filenames()
    for filename in filenames:
        if filename != ".gitkeep":
            convert_txt_to_tsv(filename)