from datetime import datetime

from six import iteritems


def format_snapshots(snapshots, category, groupings):
    return tuple(
        _label_and_count(
            snapshot['data'][category], groupings, snapshot['createdAt']
        )
        for snapshot in snapshots
    )


def _label_and_count(stats, groupings, created_at):
    data = {
        label: _sum_counts(stats, filters)
        for label, filters in iteritems(groupings)
    }
    data['created_at'] = created_at
    return data


def _sum_counts(stats, filter_by=None, sum_by='count'):
    return sum(
        statistic[sum_by] for statistic in stats
        if (not filter_by) or all(
            _check_for_inclusion(statistic.get(key), value)
            for key, value in iteritems(filter_by)
        )
    )


def _check_for_inclusion(statistic, filter_value):
    return (statistic in filter_value) if isinstance(filter_value, list) else (statistic == filter_value)
