import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Train models.")
    parser.add_argument("--config", type=str, default="", help="Path to config file.")
    parser.add_argument("--data-root", type=str, default="data", help="Data root directory.")
    args = parser.parse_args()
    print(f"config={args.config} data_root={args.data_root}")


if __name__ == "__main__":
    main()
