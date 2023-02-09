import folderstats
import pandas
import argparse
from pathlib import Path


def run():
    parser = argparse.ArgumentParser(
        description="To analyse the dataset folder and generate CSV")
    parser.add_argument('-p', '--path', dest='folderpath', type=Path, default="~/",
                        help='Folder path (default: home dir)')

    args = parser.parse_args()
    target_path = Path(args.folderpath)

    if not target_path.exists():
        print("The target directory doesn't exist")
        raise SystemExit(1)
    else:
        df = folderstats.folderstats(
            target_path, ignore_hidden=False)
        df = df.loc[(df['folder'] == True)]
        df = df.loc[df['depth'] > 0]
        folders = df['path'].values.tolist()
        df

        for folder in folders:
            df = folderstats.folderstats(
                folder, ignore_hidden=False)
            df.sort_values("name")
            df.to_csv(Path(folder).joinpath("data.csv"))
            df


if __name__ == "__main__":
    run()
