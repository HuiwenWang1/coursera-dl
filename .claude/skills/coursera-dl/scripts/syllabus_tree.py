#!/usr/bin/env python3
"""Print the module / section / lecture slugs from a coursera-dl parsed syllabus.

Usage: syllabus_tree.py <slug>-syllabus-parsed.json

The file is produced by `coursera-dl --only-syllabus --cache-syllabus <slug>`.
Use the printed section and lecture slugs with -sf / -lf.
"""
import json
import sys


def main(path):
    with open(path, encoding='utf-8') as fh:
        modules = json.load(fh)

    total = 0
    for mi, (module, sections) in enumerate(modules, 1):
        print('%02d %s' % (mi, module))
        for si, (section, lectures) in enumerate(sections, 1):
            print('   %02d %s' % (si, section))
            for li, (lecture, links) in enumerate(lectures, 1):
                formats = ','.join(sorted(links))
                print('      %02d %s  [%s]' % (li, lecture, formats))
                total += 1
    print('\n%d downloadable lectures in %d modules' % (total, len(modules)))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
