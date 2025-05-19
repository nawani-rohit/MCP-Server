from collections import Counter

# analysis of count of launches by year
def count_by_year(launches):
    counts = {}
    for launch in launches:
        year = launch.get("launch_year")
        if not year: 
            continue
        counts[year] = counts.get(year, 0) + 1
    
    year_int = sorted(int(y) for y in counts.keys())
    min_year = year_int[0]
    max_year = year_int[-1]

    filled_counts = {}
    for y in range(min_year, max_year + 1):
        filled_counts[str(y)] = counts.get(str(y), 0)
    return filled_counts

# analysis of success vs failure of launches
def success_vs_failure(launches):
    success = 0
    failure = 0
    for launch in launches:
        flag = launch.get("launch_success")
        if flag is True:
            success += 1
        elif flag is False:
            failure += 1
    return {"successful_launches": success, "failed_launches": failure}

# analysis of most frequent site
def most_frequent_site(launches):
    sites = Counter()
    for launch in launches:
        site = launch.get("launch_site", {}).get("site_name")
        if site:
            sites[site] += 1
    
    if not sites:
        return {}
    site, count = sites.most_common(1)[0]
    return {"site": site, "launch_count": count}