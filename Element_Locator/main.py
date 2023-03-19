import challenge

if __name__ == '__main__':
    print('***'*3)
    print('ORNL Code Challenge by Hyun W. Park')
    print('***' * 3)

    # define example variables
    ex_id = "3-=_+=--_~``4  3 4"
    ex_duplicates = [4, 4, 3, 2, 3, 1]

    ex_ids = ["1=.&^%uif381",
              "8 2.qerf3dsgf 5",
              "3-=_+=--_~``4  3 4",
              "7/?.F>,<=+-_)(&*(^&$623",
              "9%15^3",
              "76**23",
              "3434",
              "1381"]

    ex_specialties = [[1381, "front-end web development"],
                      [8235, "data engineering"],
                      [3434, "API design"],
                      [7623, "security"],
                      [9153, "UX"]]

    # display answers
    print('Problem 1:')
    print("{} ===> {}\n".format(ex_id, challenge.id_cleaner(ex_id)))

    print('Problem 2:')
    print("{} ===> {}\n".format(ex_duplicates, challenge.duplicate_remover(ex_duplicates)))

    print('Problem 3:')
    print('  Input IDs')
    for x in ex_ids:
        print('    {}'.format(x))
    print('  Input Specialties')
    for x in ex_specialties:
        print('    {}'.format(x))
    print("  ===> {}".format(challenge.retriever(ex_ids, ex_specialties)))
