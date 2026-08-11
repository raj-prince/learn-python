#!/usr/bin/env python3
import json
import collections

with open('projects/combined_fsspec_report.json') as f:
    data = json.load(f)

all_usages = []
for repo_data in data.get('per_repository', []):
    repo_name = repo_data.get('target_source')
    short_repo = repo_name.replace('GitHub:', '').split(' ')[0]
    for usage in repo_data.get('usages', []):
        usage['short_repo'] = short_repo
        all_usages.append(usage)

repos = [
    'dask/dask',
    'intake/intake',
    'pandas-dev/pandas',
    'pydata/xarray',
    'zarr-developers/zarr-python',
    'iterative/dvc',
    'kedro-org/kedro',
    'huggingface/datasets',
    'pytorch/pytorch',
    'Lightning-AI/pytorch-lightning',
    'pytorch/torchtitan',
    'ray-project/ray'
]

methods = collections.Counter(u['target_name'] for u in all_usages)

matrix = collections.defaultdict(lambda: collections.Counter())
for u in all_usages:
    matrix[u['target_name']][u['short_repo']] += 1

lines = []
lines.append('# Complete Cross-Repository Method Distribution Matrix (All 183 Methods)\n')
lines.append('This document provides the exact occurrence count of **every single filesystem/fsspec method call** across all 12 major Python data science and AI repositories scanned by the AST crawler.\n')
header_cols = ['Rank', 'Target Method Name', 'Total Calls'] + [r.split('/')[1] for r in repos]
lines.append('| ' + ' | '.join(header_cols) + ' |')
lines.append('| ' + ' | '.join([':---' if i < 2 else ':---:' for i in range(len(header_cols))]) + ' |')

for idx, (method, total) in enumerate(methods.most_common(), 1):
    row = [f'**{idx}**', f'`{method}`', f'**{total}**']
    for r in repos:
        cnt = matrix[method].get(r, 0)
        row.append(str(cnt) if cnt > 0 else '-')
    lines.append('| ' + ' | '.join(row) + ' |')

with open('projects/method_distribution_matrix.md', 'w') as out:
    out.write('\n'.join(lines) + '\n')

print(f'Wrote projects/method_distribution_matrix.md successfully with {len(methods)} methods!')
