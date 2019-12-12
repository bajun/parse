import time


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print '%r  %2.2f seconds' % \
              (method.__name__, (te - ts))
        return result

    return timed


def clean_names(name):
    if len(name) <= 2:
        return name

    # we don't need Ms. or Mrs. or Prof. so clean them all!
    def is_not_appeal(word):
        return False if word.endswith('.') else True

    # Also "Miss" word (looks like it's kind of honorific title)
    def is_not_miss(word):
        return True if word != 'Miss' else False

    # and we don't need 1|2-letter words
    def is_not_abbreviation(word):
        return True if len(word) > 2 else False

    # also we know that names and surnames are Capitalized Words, so we'll add istitle filter too
    filters = [is_not_appeal, is_not_miss, is_not_abbreviation, str.istitle]
    return filter(lambda x: all(f(x) for f in filters), name)
