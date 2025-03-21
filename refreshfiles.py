import pandas as pd
from enum import Enum
from dataclasses import dataclass

class RegulationType(Enum):
    REGULATION = 1
    GUIDELINE = 2

@dataclass
class Regulation:
    """
    This is a model of a WCA Regulation or Guideline. It contains the text of
    the regulation, the regulation number, and the article it belongs to.
    """
    regulation_type: RegulationType
    article: str
    regulation_number: str
    regulation_text: str

def create_anki_cards(file: str) -> None:
    """
    Create one csv file for the regulations and one for the guidelines to import into anki.

    We are reading a file containing the text from the [WCA Regulations](https://www.worldcubeassociation.org/regulations/full/).
    This file is expected to not contain any empty lines or things that are not regulations, guidelines or article numbers.
    """
    regs: list[Regulation] = []
    with open(file, 'r') as f:
        article: str = ""
        for line in f.readlines():
            line = line.rstrip()
            line_array: list[str] = line.split(" ")

            # Update article number when you encounter a new article
            if line_array[0] == 'Article':
                article = f'{line_array[0]} {line_array[1].replace(":", "")}'
                continue

            regulation_type: RegulationType = RegulationType.REGULATION if "+" not in line_array[0] else RegulationType.GUIDELINE
            regulation_number: str = line_array[0].replace(")", "")

            regulation_text: str = " ".join(line_array[1:])
            regs.append(Regulation(regulation_type, article, regulation_number, regulation_text))

    regs_df = pd.DataFrame(regs)
    regulations = regs_df[regs_df["regulation_type"] == RegulationType.REGULATION]
    guidelines = regs_df[regs_df["regulation_type"] == RegulationType.GUIDELINE]
    regulations.to_csv("regulations.csv", sep='\t', columns=["article", "regulation_number", "regulation_text"], index=False)
    guidelines.to_csv("guidelines.csv", sep='\t', columns=["article", "regulation_number", "regulation_text"], index=False)

if __name__ == '__main__':
    create_anki_cards('regs.txt')
