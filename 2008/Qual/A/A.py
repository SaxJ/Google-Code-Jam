def main():
    cases = int(input())
    for c in range(cases):
        nEngines = int(input())
        engines = []
        for e in range(nEngines):
            engine = input()
            engines.append(engine)

        nQueries = int(input())
        segment = []
        changes = 0

        for q in range(nQueries):
            query = input()
            if not (query in segment):
                if len(segment) == nEngines - 1:
                    changes += 1
                    segment = []

                segment.append(query)

        print("Case #{0}: {1}".format(c+1, changes))

if __name__ == '__main__':
    main()
