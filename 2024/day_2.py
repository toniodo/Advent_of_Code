"""Day 2 AoC 2024"""
from utils.parse import parse_number


def check_report(report: list) -> bool:
    """Check if a report is valid or not"""
    increasing: bool = (report[1] - report[0] > 0)
    # Reverse the list to have an increasing order
    if not increasing:
        report = report[::-1]
    gradient = [(j - i) for i, j in zip(report[:-1], report[1:])]
    min_value: int = min(gradient)
    if min_value <= 0:
        return False
    max_value: int = max(gradient)
    if max_value > 3:
        return False
    return True

def part_1(all_reports: list[list[int]]) -> int:
    """Compute the number of valid reports"""
    report_validity: list[bool] = [check_report(report) for report in all_reports]
    print("The number of valid reports is:", sum(report_validity))

def check_tolerate_report(report: list) -> bool:
    """Check if a report is valid or not with a tolerance of 1"""
    for i in range(len(report)):
        tmp_report = report.copy()
        tmp_report.pop(i)
        if check_report(tmp_report):
            return True
    return False

def part_2(all_reports: list[list[int]]) -> int:
    """Compute the number of valid reports with a tolerance of 1"""
    report_validity: list[bool] = [check_tolerate_report(report) for report in all_reports]
    print("The number of valid reports with tolerance is:", sum(report_validity))


if __name__ =='__main__':
    all_lines = parse_number("inputs/2.txt")
    part_1(all_lines)
    part_2(all_lines)
