def solution(strings, n):
    return sorted(sorted(strings),key=lambda a:a[n])
    