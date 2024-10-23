import asyncio
import argparse
from code_collector.collector import collect_user_code
from code_collector.utils import get_default_extensions, get_project_root

def main():
    parser = argparse.ArgumentParser(description="Collect user-written code from a project directory.")
    parser.add_argument("directory", nargs="?", default=get_project_root(), help="Project directory path")
    parser.add_argument("-e", "--extensions", nargs="+", default=get_default_extensions(), help="File extensions to include")
    parser.add_argument("-i", "--ignore", default=".gitignore", help="Ignore file path")
    parser.add_argument("-o", "--output", default="user_code.txt", help="Output file name")

    args = parser.parse_args()

    asyncio.run(collect_user_code(args.directory, args.extensions, args.ignore, args.output))
    print(f"User code collected and saved to {args.output}")

if __name__ == "__main__":
    main()