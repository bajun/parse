import re
import urllib2
from collections import Counter
from multiprocessing import Pool, cpu_count

from helpers import timeit, clean_names, prepare_chunks


def get_data(n):
    return get_data_wrapped(n)


def get_data_wrapped(n):
    names = Counter()
    url = "http://www.namefake.com"
    i = 0
    while i < n:
        try:
            response = urllib2.urlopen(url, timeout=1)
            data = response.read()
            match = re.search(r"<h2>(.*)<\/h2>", data)
            if match:
                _names = match.group(1).split(' ')
                for name in clean_names(_names):
                    names.update({name: 1})
                i += 1
        except IOError as e:
            pass

    return names


@timeit
def parse(times):
    temp_res = []
    proc_num = cpu_count() * 2
    chunks = prepare_chunks(times, proc_num)
    # in this block we spawn our process for the number AND for remainder of our approximated count
    pool = Pool(processes=proc_num + 1)
    temp_res += pool.map(get_data, chunks)
    return temp_res


if __name__ == '__main__':
    parsed_names = parse(100)
    count = sum(parsed_names, Counter())
    print '\r\n'.join(['%s %d' % (x[0], x[1]) for x in count.most_common(10)])
