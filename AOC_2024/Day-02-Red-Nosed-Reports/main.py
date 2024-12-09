import typing


def read_reports(file_path: str) -> typing.List[typing.List[int]]:
    with open(file_path, "r") as f:
        return [[int(z) for z in line.split()] for line in f]


def is_safe(report: typing.List[int]) -> bool:
    return all(
        1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1)
    ) or all(1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))


def can_be_safe(report: typing.List[int]) -> bool:
    return any(is_safe(report[:i] + report[i + 1 :]) for i in range(len(report)))


def main(file_path: str):
    reports = read_reports(file_path)

    # Part 1: Count safe reports
    safe_count = sum(map(is_safe, reports))
    print(f"Part 1 Safe Count: {safe_count}")

    # Part 2: Count reports that are safe or can be made safe
    safe_count2 = sum(is_safe(report) or can_be_safe(report) for report in reports)
    print(f"Part 2 Safe Count: {safe_count2}")


if __name__ == "__main__":
    main("../data/day2-1-test.txt")
